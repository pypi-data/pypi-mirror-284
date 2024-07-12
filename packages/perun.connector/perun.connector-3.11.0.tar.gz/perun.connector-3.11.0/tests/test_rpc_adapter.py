import copy
import logging
from unittest.mock import MagicMock, mock_open, patch

import pytest

from perun.connector import perun_openapi
from perun.connector.adapters.PerunRpcAdapter import PerunRpcAdapter
from perun.connector.models.Facility import Facility
from perun.connector.models.Group import Group
from perun.connector.models.Member import Member
from perun.connector.models.MemberStatusEnum import MemberStatusEnum
from perun.connector.models.Resource import Resource
from perun.connector.models.User import User
from perun.connector.models.UserExtSource import UserExtSource
from perun.connector.models.VO import VO
from perun.connector.perun_openapi.exceptions import ApiException
from perun.connector.utils.ConfigStore import ConfigStore


class HttpResponse:
    def __init__(self, input_data: str):
        self.status = None
        self.data = input_data
        self.reason = None

    def getheaders(self):
        return "headers"


CONFIG = ConfigStore.get_openapi_config()

COOKIE_FILEPATH = CONFIG.get("cookie_filepath", "cookie.txt")

# sample groups - external representation (Devel)
TEST_GROUP_EXTERNAL_REPRESENTATION_1 = {
    "id": 1,
    "vo_id": 10,
    "uuid": "sample-uuid-value",
    "name": "sample:group:name",
    "description": "This is a sample group",
}

TEST_GROUP_EXTERNAL_REPRESENTATION_2 = {
    "id": 2,
    "vo_id": 10,
    "uuid": "sample-uuid-value-2",
    "name": "sample:group:name:specific",
    "description": "This is a sample sub-group",
}

# sample groups - internal representation

TEST_VO = VO(62, "CESNET e-infrastruktura", "einfra")
TEST_MEMBER_INTERNAL_REPRESENTATION = Member(5, TEST_VO, "VALID")
TEST_MEMBER_EXTERNAL_REPRESENTATION = {"id": 5, "vo_id": TEST_VO.id, "status": "VALID"}
TEST_USER = User(10, "John Doe")
SAMPLE_SHORT_GROUP_NAME = "short_name"

TEST_GROUP_INTERNAL_REPRESENTATION_1 = Group(
    TEST_GROUP_EXTERNAL_REPRESENTATION_1["id"],
    TEST_VO,
    TEST_GROUP_EXTERNAL_REPRESENTATION_1["uuid"],
    TEST_GROUP_EXTERNAL_REPRESENTATION_1["name"],
    f"{SAMPLE_SHORT_GROUP_NAME}:" f'{TEST_GROUP_EXTERNAL_REPRESENTATION_1["name"]}',
    TEST_GROUP_EXTERNAL_REPRESENTATION_1["description"],
)

TEST_GROUP_INTERNAL_REPRESENTATION_2 = Group(
    TEST_GROUP_EXTERNAL_REPRESENTATION_2["id"],
    TEST_VO,
    TEST_GROUP_EXTERNAL_REPRESENTATION_2["uuid"],
    TEST_GROUP_EXTERNAL_REPRESENTATION_2["name"],
    f"{SAMPLE_SHORT_GROUP_NAME}:" f'{TEST_GROUP_EXTERNAL_REPRESENTATION_2["name"]}',
    TEST_GROUP_EXTERNAL_REPRESENTATION_2["description"],
)

# sample Facility
TEST_RP_IDENTIFIER_1 = "test rp identifier"
TEST_RP_IDENTIFIER_2 = "test rp identifier 2"

TEST_EXTERNAL_FACILITY_1 = {
    "id": 1,
    "name": "test name",
    "description": "test description",
}
TEST_EXTERNAL_FACILITY_2 = {
    "id": 2,
    "name": "test name 2",
    "description": "test description 2",
}

TEST_EXTERNAL_FACILITY_WITH_ATTRS_1 = [
    {
        "facility": {
            "id": 1,
            "name": "test name",
            "description": "test description",
        },
        "attributes": [
            {
                "baseFriendlyName": "rpIdentifier",
                "base_friendly_name": "rpIdentifier",
                "bean_name": "Attribute",
                "description": "Unique identifier of RP",
                "displayName": "RP Identifier",
                "display_name": "RP Identifier",
                "entity": "facility",
                "friendlyName": "rpIdentifier",
                "friendlyNameParameter": "",
                "friendly_name": "rpIdentifier",
                "friendly_name_parameter": "",
                "namespace": "urn:perun:facility:attribute-def:def",
                "type": "java.lang.String",
                "unique": True,
                "value": TEST_RP_IDENTIFIER_1,
                "writable": True,
            }
        ],
    }
]

TEST_SINGLE_PERUN_FACILITY = [TEST_EXTERNAL_FACILITY_1]
TEST_MULTIPLE_PERUN_FACILITIES = [TEST_EXTERNAL_FACILITY_1, TEST_EXTERNAL_FACILITY_2]

TEST_INTERNAL_FACILITY_1 = Facility(
    TEST_EXTERNAL_FACILITY_1["id"],
    TEST_EXTERNAL_FACILITY_1["name"],
    TEST_EXTERNAL_FACILITY_1["description"],
    TEST_RP_IDENTIFIER_1,
    {},
)

TEST_INTERNAL_FACILITY_2 = Facility(
    TEST_EXTERNAL_FACILITY_2["id"],
    TEST_EXTERNAL_FACILITY_2["name"],
    TEST_EXTERNAL_FACILITY_2["description"],
    TEST_RP_IDENTIFIER_2,
    {},
)

MULTIPLE_ATTRS_ERROR_TEXT = (
    f"There is more than one facility with rpID '" f"{TEST_RP_IDENTIFIER_1}'."
)
NO_ATTRS_ERROR_TEXT = f"No facility with rpID '{TEST_RP_IDENTIFIER_1}' found."

COOKIE = "PERUNSESSION=TEST_COOKIE;"
RESPONSE_HEADER_COOKIE = {"Set-Cookie": COOKIE}


def get_entity_specific_attributes(attribute_type: str):
    generated_attrs = []
    attr_names = []
    attr_values = []
    attr_namespaces = []

    if attribute_type == "user":
        attr_names = [
            "perunUserAttribute_phone",
            "perunUserAttribute_groupNames",
            "perunUserAttribute_preferredLanguage",
        ]
        attr_values = [
            None,
            ["group 1 name", "group 2 name"],
            "sample attribute value 3",
        ]
        attr_namespaces = [
            "urn:perun:user:attribute-def:def",
            "urn:perun:user:attribute-def:virt",
            "urn:perun:user:attribute-def:def",
        ]

    elif attribute_type == "vo":
        attr_names = ["perunVoAttribute_aup"]
        attr_values = ["sample value"]
        attr_namespaces = ["urn:perun:vo:attribute-def:def"]

    elif attribute_type == "entityless":
        attr_names = [
            "perunEntitylessAttribute_orgAups",
            "perunEntitylessAttribute_orgAups",
        ]
        attr_values = [None, "sample attribute value"]
        attr_namespaces = [
            "urn:perun:entityless:attribute-def:def",
            "urn:perun:entityless:attribute-def:def",
        ]

    elif attribute_type == "facility":
        attr_names = ["perunFacilityAttr_checkGroupMembership"]
        attr_values = ["test value"]
        attr_namespaces = ["urn:perun:facility:attribute-def:def"]

    for index, attr_name in enumerate(attr_names):
        generated_attrs.append(
            {
                "id": index,
                "name": attr_name,
                "namespace": attr_namespaces[index],
                "display_name": f"display name for {attr_name}",
                "type": "some type",
                "value": attr_values[index],
                "friendlyName": attr_name.split("_")[-1],
            }
        )

    return generated_attrs


@patch(
    "perun.connector.perun_openapi.api.users_manager_api.UsersManagerApi"
    ".get_user_by_ext_source_name_and_ext_login"
)
@patch("builtins.open", new_callable=mock_open, read_data="")
def test_get_perun_user_with_middle_name_and_title_before_after(
    mock_cookie, mock_request_1
):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    user_with_middle_name_title_before_after = {
        "id": 10,
        "title_before": "Ing.",
        "first_name": "John",
        "middle_name": "Frederick",
        "last_name": "Doe",
        "title_after": "Ph.D.",
    }
    perun_openapi.api.users_manager_api.UsersManagerApi.get_user_by_ext_source_name_and_ext_login = MagicMock(
        return_value=(
            user_with_middle_name_title_before_after,
            200,
            RESPONSE_HEADER_COOKIE,
        )
    )

    expected_user = User(10, "Ing. John Frederick Doe Ph.D.")
    result_user = adapter.get_perun_user("10", ["John Doe"])

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result_user == expected_user


@patch(
    "perun.connector.perun_openapi.api.users_manager_api.UsersManagerApi"
    ".get_user_by_ext_source_name_and_ext_login"
)
@patch("builtins.open", new_callable=mock_open, read_data="")
def test_get_perun_user_without_middle_name_and_title_before_after(
    mock_cookie, mock_request_1
):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    user_without_middle_name_title_before_after = {
        "id": 10,
        "title_before": "Ing.",
        "first_name": "John",
        "middle_name": None,
        "last_name": "Doe",
        "title_after": "Ph.D.",
    }
    perun_openapi.api.users_manager_api.UsersManagerApi.get_user_by_ext_source_name_and_ext_login = MagicMock(
        return_value=(
            user_without_middle_name_title_before_after,
            200,
            RESPONSE_HEADER_COOKIE,
        )
    )

    expected_user = User(10, "Ing. John Doe Ph.D.")
    result_user = adapter.get_perun_user("10", ["John Doe"])

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result_user == expected_user


@patch(
    "perun.connector.perun_openapi.api.users_manager_api.UsersManagerApi"
    ".get_user_by_ext_source_name_and_ext_login"
)
@patch("builtins.open", new_callable=mock_open)
def test_user_without_middle_name_and_title_before(mock_cookie, mock_request_1):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    user_without_middle_name_title_before = {
        "id": 10,
        "title_before": "Ing.",
        "first_name": "John",
        "middle_name": None,
        "last_name": "Doe",
        "title_after": None,
    }

    perun_openapi.api.users_manager_api.UsersManagerApi.get_user_by_ext_source_name_and_ext_login = MagicMock(
        return_value=(
            user_without_middle_name_title_before,
            200,
            RESPONSE_HEADER_COOKIE,
        )
    )

    expected_user = User(10, "Ing. John Doe")
    result_user = adapter.get_perun_user("10", ["John Doe"])

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result_user == expected_user


@patch(
    "perun.connector.perun_openapi.api.users_manager_api.UsersManagerApi"
    ".get_user_by_ext_source_name_and_ext_login"
)
@patch("builtins.open", new_callable=mock_open)
def test_user_without_middle_name_and_title_after(mock_cookie, mock_request_1):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    user_without_middle_name_title_after = {
        "id": 10,
        "title_before": None,
        "first_name": "John",
        "middle_name": None,
        "last_name": "Doe",
        "title_after": "Ph.D.",
    }

    perun_openapi.api.users_manager_api.UsersManagerApi.get_user_by_ext_source_name_and_ext_login = MagicMock(
        return_value=(user_without_middle_name_title_after, 200, RESPONSE_HEADER_COOKIE)
    )

    expected_user = User(10, "John Doe Ph.D.")
    result_user = adapter.get_perun_user("10", ["John Doe"])

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result_user == expected_user


@patch(
    "perun.connector.perun_openapi.api.users_manager_api.UsersManagerApi"
    ".get_user_by_ext_source_name_and_ext_login"
)
@patch("builtins.open", new_callable=mock_open)
def test_user_without_middle_name_and_titles(mock_cookie, mock_request_1):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    user_without_middle_name_and_titles = {
        "id": 10,
        "title_before": None,
        "first_name": "John",
        "middle_name": None,
        "last_name": "Doe",
        "title_after": None,
    }

    perun_openapi.api.users_manager_api.UsersManagerApi.get_user_by_ext_source_name_and_ext_login = MagicMock(
        return_value=(user_without_middle_name_and_titles, 200, RESPONSE_HEADER_COOKIE)
    )

    expected_user = User(10, "John Doe")
    result_user = adapter.get_perun_user("10", ["John Doe"])

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result_user == expected_user


# get_get_member_groups tests
@patch(
    "perun.connector.perun_openapi.api.attributes_manager_api.AttributesManagerApi"
    ".get_attribute"
)
@patch(
    "perun.connector.perun_openapi.api.groups_manager_api.GroupsManagerApi"
    ".get_all_member_groups"
)
@patch(
    "perun.connector.perun_openapi.api.members_manager_api.MembersManagerApi"
    ".get_member_by_user"
)
@patch("perun.connector.perun_openapi.api.vos_manager_api.VosManagerApi.get_vo_by_id")
@patch("builtins.open", new_callable=mock_open)
def test_get_member_groups_found_member_groups(
    mock_cookie, mock_request_1, mock_request_2, mock_request_3, mock_request_4
):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    perun_openapi.api.attributes_manager_api.AttributesManagerApi.get_attribute = (
        MagicMock(
            return_value=(
                {"value": SAMPLE_SHORT_GROUP_NAME},
                200,
                RESPONSE_HEADER_COOKIE,
            )
        )
    )

    perun_openapi.api.vos_manager_api.VosManagerApi.get_vo_by_id = MagicMock(
        return_value=(TEST_VO, 200, RESPONSE_HEADER_COOKIE)
    )

    perun_openapi.api.groups_manager_api.GroupsManagerApi.get_all_member_groups = (
        MagicMock(
            return_value=(
                [
                    TEST_GROUP_EXTERNAL_REPRESENTATION_1,
                    TEST_GROUP_EXTERNAL_REPRESENTATION_2,
                ],
                200,
                RESPONSE_HEADER_COOKIE,
            )
        )
    )

    perun_openapi.api.members_manager_api.MembersManagerApi.get_member_by_user = (
        MagicMock(
            return_value=(
                TEST_MEMBER_INTERNAL_REPRESENTATION.__dict__,
                200,
                RESPONSE_HEADER_COOKIE,
            )
        )
    )

    result_groups = adapter.get_member_groups(user=TEST_USER, vo=TEST_VO)

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert [
        TEST_GROUP_INTERNAL_REPRESENTATION_1,
        TEST_GROUP_INTERNAL_REPRESENTATION_2,
    ] == result_groups


@patch(
    "perun.connector.perun_openapi.api.members_manager_api.MembersManagerApi"
    ".get_member_by_user"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_member_groups_member_not_found(mock_cookie, mock_request_1):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    perun_openapi.api.members_manager_api.MembersManagerApi.get_member_by_user = (
        MagicMock(return_value=(None, 200, RESPONSE_HEADER_COOKIE))
    )

    result_groups = adapter.get_member_groups(user=TEST_USER, vo=TEST_VO)

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result_groups == []


@patch(
    "perun.connector.perun_openapi.api.attributes_manager_api.AttributesManagerApi"
    ".get_attribute"
)
@patch(
    "perun.connector.perun_openapi.api.facilities_manager_api.FacilitiesManagerApi"
    ".get_assigned_resources_for_facility"
)
@patch(
    "perun.connector.perun_openapi.api.resources_manager_api.ResourcesManagerApi"
    ".get_assigned_groups"
)
@patch("perun.connector.perun_openapi.api.vos_manager_api.VosManagerApi.get_vo_by_id")
@patch("builtins.open", new_callable=mock_open)
def test_get_sp_groups_found_sp_groups(
    mock_cookie, mock_request_1, mock_request_2, mock_request_3, mock_request_4
):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    test_resources = [Resource(1, None, None, None)]

    perun_openapi.api.attributes_manager_api.AttributesManagerApi.get_attribute = (
        MagicMock(
            return_value=(
                {"value": SAMPLE_SHORT_GROUP_NAME},
                200,
                RESPONSE_HEADER_COOKIE,
            )
        )
    )

    perun_openapi.api.facilities_manager_api.FacilitiesManagerApi.get_assigned_resources_for_facility = MagicMock(
        return_value=(test_resources, 200, RESPONSE_HEADER_COOKIE)
    )

    perun_openapi.api.resources_manager_api.ResourcesManagerApi.get_assigned_groups = (
        MagicMock(
            return_value=(
                [
                    TEST_GROUP_EXTERNAL_REPRESENTATION_1,
                    TEST_GROUP_EXTERNAL_REPRESENTATION_1,
                    TEST_GROUP_EXTERNAL_REPRESENTATION_2,
                    TEST_GROUP_EXTERNAL_REPRESENTATION_2,
                ],
                200,
                RESPONSE_HEADER_COOKIE,
            )
        )
    )

    perun_openapi.api.vos_manager_api.VosManagerApi.get_vo_by_id = MagicMock(
        return_value=(TEST_VO, 200, RESPONSE_HEADER_COOKIE)
    )

    result_groups = adapter.get_sp_groups_by_facility(TEST_INTERNAL_FACILITY_1)

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert [
        TEST_GROUP_INTERNAL_REPRESENTATION_1,
        TEST_GROUP_INTERNAL_REPRESENTATION_2,
    ] == result_groups


def test_get_sp_groups_no_input_facility():
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    result_groups = adapter.get_sp_groups_by_facility(None)
    assert result_groups == []


@patch(
    "perun.connector.perun_openapi.api.facilities_manager_api.FacilitiesManagerApi"
    ".get_assigned_resources_for_facility"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_sp_groups_no_resources_found(mock_cookie, mock_request_1):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    perun_openapi.api.facilities_manager_api.FacilitiesManagerApi.get_assigned_resources_for_facility = MagicMock(
        return_value=([], 200, RESPONSE_HEADER_COOKIE)
    )

    result_groups = adapter.get_sp_groups_by_facility(TEST_INTERNAL_FACILITY_1)

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result_groups == []


@patch("perun.connector.perun_openapi.api.vos_manager_api.VosManagerApi.get_vo_by_id")
@patch(
    "perun.connector.perun_openapi.api.attributes_manager_api.AttributesManagerApi"
    ".get_attribute"
)
@patch(
    "perun.connector.perun_openapi.api.groups_manager_api.GroupsManagerApi.get_group_by_name"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_group_by_name(mock_cookie, mock_request_1, mock_request_2, mock_request_3):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    perun_openapi.api.vos_manager_api.VosManagerApi.get_vo_by_id = MagicMock(
        return_value=(TEST_VO, 200, RESPONSE_HEADER_COOKIE)
    )

    perun_openapi.api.attributes_manager_api.AttributesManagerApi.get_attribute = (
        MagicMock(
            return_value=(
                {"value": SAMPLE_SHORT_GROUP_NAME},
                200,
                RESPONSE_HEADER_COOKIE,
            )
        )
    )

    perun_openapi.api.groups_manager_api.GroupsManagerApi.get_group_by_name = MagicMock(
        return_value=(TEST_GROUP_EXTERNAL_REPRESENTATION_1, 200, RESPONSE_HEADER_COOKIE)
    )

    result = adapter.get_group_by_name(TEST_VO, "sample name")

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result == TEST_GROUP_INTERNAL_REPRESENTATION_1


@patch("perun.connector.perun_openapi.api.vos_manager_api.VosManagerApi.get_vo_by_id")
@patch(
    "perun.connector.perun_openapi.api.vos_manager_api.VosManagerApi.get_vo_by_short_name"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_vo_correct_arguments(mock_cookie, mock_request_1, mock_request_2):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    test_vo_id = 1
    test_vo_short_name = "sample short name"
    test_vo = VO(test_vo_id, "sample name", test_vo_short_name)

    perun_openapi.api.vos_manager_api.VosManagerApi.get_vo_by_id = MagicMock(
        return_value=(test_vo, 200, RESPONSE_HEADER_COOKIE)
    )
    perun_openapi.api.vos_manager_api.VosManagerApi.get_vo_by_short_name = MagicMock(
        return_value=(test_vo, 200, RESPONSE_HEADER_COOKIE)
    )

    obtained_vo_by_id = adapter.get_vo(vo_id=test_vo_id)
    obtained_vo_by_short_name = adapter.get_vo(short_name=test_vo_short_name)

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert test_vo == obtained_vo_by_id
    assert test_vo == obtained_vo_by_short_name


def test_get_vo_no_arguments():
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    no_args_error_message = (
        "Neither short_name nor id was provided, "
        "please specify exactly one to find VO by."
    )

    with pytest.raises(ValueError) as error:
        _ = adapter.get_vo()

        assert str(error.value.args[0]) == no_args_error_message


def test_get_vo_too_many_arguments():
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    too_many_args_error_message = (
        "VO can be obtained either by its "
        "short_name or id, not both at the same "
        "time."
    )

    with pytest.raises(ValueError) as error:
        _ = adapter.get_vo(vo_id=1, short_name="sample short name")
        assert str(error.value.args[0]) == too_many_args_error_message


@patch(
    "perun.connector.perun_openapi.api.attributes_manager_api.AttributesManagerApi"
    ".get_facility_attributes_by_names"
)
@patch("perun.connector.perun_openapi.api.searcher_api.SearcherApi" ".get_facilities")
@patch("builtins.open", new_callable=mock_open)
def test_get_facilities_by_attribute_value_correct_attribute(
    mock_cookie, mock_request_1, mock_request_2
):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    perun_openapi.api.searcher_api.SearcherApi.get_facilities = MagicMock(
        return_value=(TEST_SINGLE_PERUN_FACILITY, 200, RESPONSE_HEADER_COOKIE)
    )

    perun_openapi.api.attributes_manager_api.AttributesManagerApi.get_facility_attributes_by_names = MagicMock(
        return_value=(
            [
                {
                    "id": "test id",
                    "name": "test name",
                    "display_name": "test display name",
                    "type": "test type",
                    "value": TEST_INTERNAL_FACILITY_1.rp_id,
                    "namespace": "urn:perun:facility:attribute-def:def",
                    "friendlyName": "rpIdentifier",
                }
            ],
            200,
            RESPONSE_HEADER_COOKIE,
        )
    )

    attribute = {"test name": "test value"}
    result_facilities = adapter.get_facilities_by_attribute_value(attribute)

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result_facilities == [TEST_INTERNAL_FACILITY_1]


def test_get_facilities_by_attribute_value_empty_attribute(caplog):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    empty_attribute = {}
    wrong_number_of_attrs_error_text = (
        f"Attribute must contain exactly one "
        f"name and one value. Given attribute "
        f""
        f""
        f'contains: "{empty_attribute}".'
    )

    with caplog.at_level(logging.WARNING):
        result_facilities = adapter.get_facilities_by_attribute_value(empty_attribute)
        assert result_facilities == []
        assert wrong_number_of_attrs_error_text in caplog.text


def test_get_facilities_by_attribute_value_too_many_attributes(caplog):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    multiple_attributes = {"test name": "test value", "test name 2": "test value 2"}
    wrong_number_of_attrs_error_text = (
        f"Attribute must contain exactly one "
        f"name and one value. Given attribute "
        f""
        f""
        f'contains: "{multiple_attributes}".'
    )

    with caplog.at_level(logging.WARNING):
        result_facilities = adapter.get_facilities_by_attribute_value(
            multiple_attributes
        )
        assert result_facilities == []
        assert wrong_number_of_attrs_error_text in caplog.text


@patch(
    "perun.connector.perun_openapi.api.facilities_manager_api.FacilitiesManagerApi"
    ".get_facilities_by_attribute"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_facility_by_rp_identifier_found_facility(mock_cookie, mock_request_1):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    perun_openapi.api.facilities_manager_api.FacilitiesManagerApi.get_facilities_by_attribute = MagicMock(
        return_value=(TEST_SINGLE_PERUN_FACILITY, 200, RESPONSE_HEADER_COOKIE)
    )

    result_facility = adapter.get_facility_by_rp_identifier(TEST_RP_IDENTIFIER_1)

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result_facility == TEST_INTERNAL_FACILITY_1


@patch(
    "perun.connector.perun_openapi.api.facilities_manager_api.FacilitiesManagerApi"
    ".get_facilities_by_attribute"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_facility_by_rp_identifier_no_perun_attr_found(
    mock_cookie, mock_request_1, caplog
):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    perun_openapi.api.facilities_manager_api.FacilitiesManagerApi.get_facilities_by_attribute = MagicMock(
        return_value=(None, 200, RESPONSE_HEADER_COOKIE)
    )
    expected_error_message = "No facility with rpID 'test rp identifier' found."

    with pytest.raises(Exception) as error:
        _ = adapter.get_facility_by_rp_identifier(TEST_RP_IDENTIFIER_1)

        mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
        mock_cookie().write.assert_called_with(COOKIE)

        assert str(error.value.args[0]) == expected_error_message


@patch(
    "perun.connector.perun_openapi.api.facilities_manager_api.FacilitiesManagerApi"
    ".get_facilities_by_attribute"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_facility_by_rp_identifier_multiple_perun_attrs_found(
    mock_cookie, mock_request_1, caplog
):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    perun_openapi.api.facilities_manager_api.FacilitiesManagerApi.get_facilities_by_attribute = MagicMock(
        return_value=(TEST_MULTIPLE_PERUN_FACILITIES, 200, RESPONSE_HEADER_COOKIE)
    )

    expected_error_message = (
        "There is more than one facility with rpID 'test rp identifier'."
    )

    with pytest.raises(Exception) as error:
        _ = adapter.get_facility_by_rp_identifier(TEST_RP_IDENTIFIER_1)

        mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
        mock_cookie().write.assert_called_with(COOKIE)

        assert str(error.value.args[0]) == expected_error_message


@patch(
    "perun.connector.perun_openapi.api.users_manager_api.UsersManagerApi"
    ".get_groups_for_facility_where_user_is_active"
)
@patch(
    "perun.connector.perun_openapi.api.attributes_manager_api.AttributesManagerApi"
    ".get_attribute"
)
@patch("perun.connector.perun_openapi.api.vos_manager_api.VosManagerApi.get_vo_by_id")
@patch("builtins.open", new_callable=mock_open)
def test_get_users_groups_on_facility_multiple_groups_found(
    mock_cookie, mock_request_1, mock_request_2, mock_request_3
):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    perun_openapi.api.users_manager_api.UsersManagerApi.get_groups_for_facility_where_user_is_active = MagicMock(
        return_value=(
            [
                TEST_GROUP_EXTERNAL_REPRESENTATION_1,
                TEST_GROUP_EXTERNAL_REPRESENTATION_2,
                TEST_GROUP_EXTERNAL_REPRESENTATION_2,
                TEST_GROUP_EXTERNAL_REPRESENTATION_1,
                TEST_GROUP_EXTERNAL_REPRESENTATION_1,
            ],
            200,
            RESPONSE_HEADER_COOKIE,
        )
    )

    perun_openapi.api.attributes_manager_api.AttributesManagerApi.get_attribute = (
        MagicMock(
            return_value=(
                {"value": SAMPLE_SHORT_GROUP_NAME},
                200,
                RESPONSE_HEADER_COOKIE,
            )
        )
    )

    perun_openapi.api.vos_manager_api.VosManagerApi.get_vo_by_id = MagicMock(
        return_value=(TEST_VO, 200, RESPONSE_HEADER_COOKIE)
    )

    result_groups = adapter.get_users_groups_on_facility(
        TEST_INTERNAL_FACILITY_1, TEST_USER
    )

    for group in result_groups:
        assert isinstance(group, Group)

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert [
        TEST_GROUP_INTERNAL_REPRESENTATION_1,
        TEST_GROUP_INTERNAL_REPRESENTATION_2,
    ] == result_groups


def test_get_users_groups_on_facility_no_input_facility():
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    result_groups = adapter.get_users_groups_on_facility(None, TEST_USER)

    assert result_groups == []


@patch(
    "perun.connector.perun_openapi.api.users_manager_api.UsersManagerApi"
    ".get_groups_for_facility_where_user_is_active"
)
@patch(
    "perun.connector.perun_openapi.api.attributes_manager_api.AttributesManagerApi"
    ".get_attribute"
)
@patch("perun.connector.perun_openapi.api.vos_manager_api.VosManagerApi.get_vo_by_id")
@patch("builtins.open", new_callable=mock_open)
def test_get_users_groups_on_facility_no_groups_found(
    mock_cookie, mock_request_1, mock_request_2, mock_request_3
):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    perun_openapi.api.users_manager_api.UsersManagerApi.get_groups_for_facility_where_user_is_active = MagicMock(
        return_value=([], 200, RESPONSE_HEADER_COOKIE)
    )

    perun_openapi.api.attributes_manager_api.AttributesManagerApi.get_attribute = (
        MagicMock(
            return_value=(
                {"value": SAMPLE_SHORT_GROUP_NAME},
                200,
                RESPONSE_HEADER_COOKIE,
            )
        )
    )

    perun_openapi.api.vos_manager_api.VosManagerApi.get_vo_by_id = MagicMock(
        return_value=(TEST_VO, 200, RESPONSE_HEADER_COOKIE)
    )

    result_groups = adapter.get_users_groups_on_facility(
        TEST_INTERNAL_FACILITY_1, TEST_USER
    )

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result_groups == []


@patch(
    "perun.connector.perun_openapi.api.attributes_manager_api.AttributesManagerApi"
    ".get_facilities_by_attribute_with_attributes"
)
@patch("builtins.open", new_callable=mock_open)
def get_facilities_by_attribute_with_attributes_correct_attribute(
    mock_cookie, mock_request_1, mock_request_2
):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    perun_openapi.api.searcher_api.SearcherApi.get_facilities = MagicMock(
        return_value=(TEST_SINGLE_PERUN_FACILITY, 200, RESPONSE_HEADER_COOKIE)
    )

    perun_openapi.api.attributes_manager_api.AttributesManagerApi.get_facilities_by_attribute_with_attributes = MagicMock(
        return_value=(TEST_EXTERNAL_FACILITY_WITH_ATTRS_1, 200, RESPONSE_HEADER_COOKIE)
    )

    result_facilities = adapter.get_facilities_by_attribute_with_attributes(
        "test name", "test value", ["urn:perun:facility:attribute-def:def:rpIdentifier"]
    )

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result_facilities == [TEST_INTERNAL_FACILITY_1]


@patch(
    "perun.connector.perun_openapi.api.users_manager_api.UsersManagerApi"
    ".get_user_by_ext_source_name_and_ext_login"
)
@patch("perun.connector.adapters.PerunRpcAdapter.PerunRpcAdapter.get_perun_user")
@patch("builtins.open", new_callable=mock_open)
def test_get_user_ext_source(mock_cookie, mock_request_1, mock_request_2):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    source_id = 1
    source_login = "john@src"
    source_name = "sample source name"
    user_ext_source_external_representation = {
        "id": source_id,
        "login": source_login,
        "ext_source": {"name": source_name},
    }

    user_ext_source_internal_representation = UserExtSource(
        source_id, source_name, source_login, TEST_USER
    )

    perun_openapi.api.users_manager_api.UsersManagerApi.get_user_ext_source_by_ext_login_and_ext_source_name = MagicMock(
        return_value=(
            user_ext_source_external_representation,
            200,
            RESPONSE_HEADER_COOKIE,
        )
    )

    PerunRpcAdapter.get_perun_user = MagicMock(return_value=TEST_USER)

    result_ext_source = adapter.get_user_ext_source(source_name, source_login)

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result_ext_source == user_ext_source_internal_representation


@patch(
    "perun.connector.perun_openapi.api.attributes_manager_api.AttributesManagerApi"
    ".get_user_ext_source_attributes_by_names"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_user_ext_source_attributes_multiple_attributes(
    mock_cookie, mock_request_1
):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    test_attr_1_name = "perunUserAttribute_givenName"
    test_attribute_1 = {
        "id": 1,
        "name": test_attr_1_name,
        "namespace": "urn:perun:ues:attribute-def:def",
        "display_name": "sample attribute name 1",
        "type": "test type 1",
        "value": "sample attribute value 1",
        "friendlyName": "givenName",
    }

    test_attr_2_name = "perunUserAttribute_sn"
    test_attribute_2 = {
        "id": 2,
        "name": test_attr_2_name,
        "namespace": "urn:perun:ues:attribute-def:def",
        "display_name": "sample attribute name 2",
        "type": "test type 2",
        "value": "sample attribute value 2",
        "friendlyName": "sn",
    }

    attribute_names = [
        test_attribute_1["namespace"] + ":" + test_attribute_1["friendlyName"],
        test_attribute_2["namespace"] + ":" + test_attribute_2["friendlyName"],
    ]
    ext_source = UserExtSource(1, "sample name", "sample login", None)

    expected_attribute_1 = test_attribute_1.copy()

    expected_attribute_2 = test_attribute_2.copy()

    perun_openapi.api.attributes_manager_api.AttributesManagerApi.get_user_ext_source_attributes_by_names = MagicMock(
        return_value=([test_attribute_1, test_attribute_2], 200, RESPONSE_HEADER_COOKIE)
    )

    result_attrs = adapter.get_user_ext_source_attributes(ext_source, attribute_names)
    expected_attrs = {
        attribute_names[0]: expected_attribute_1["value"],
        attribute_names[1]: expected_attribute_2["value"],
    }

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result_attrs == expected_attrs


@patch(
    "perun.connector.perun_openapi.api.attributes_manager_api.AttributesManagerApi"
    ".get_user_ext_source_attributes_by_names"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_user_ext_source_attributes_no_attributes(mock_cookie, mock_request_1):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    perun_openapi.api.attributes_manager_api.AttributesManagerApi.get_user_ext_source_attributes_by_names = MagicMock(
        return_value=([], 200, RESPONSE_HEADER_COOKIE)
    )

    ext_source = UserExtSource(1, "sample name", "sample login", None)
    result_attrs = adapter.get_user_ext_source_attributes(ext_source, [])

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result_attrs == {}


@patch(
    "perun.connector.perun_openapi.api.members_manager_api.MembersManagerApi"
    ".get_member_by_user"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_member_status_by_user_and_vo_valid_member(mock_cookie, mock_request_1):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    expected_status = "VALID"
    test_member_external_representation = {"id": 1, "status": expected_status}
    perun_openapi.api.members_manager_api.MembersManagerApi.get_member_by_user = (
        MagicMock(
            return_value=(
                test_member_external_representation,
                200,
                RESPONSE_HEADER_COOKIE,
            )
        )
    )

    result_status = adapter.get_member_status_by_user_and_vo(TEST_USER, TEST_VO)

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result_status == MemberStatusEnum(expected_status)


@patch(
    "perun.connector.perun_openapi.api.members_manager_api.MembersManagerApi"
    ".get_member_by_user"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_member_status_by_user_and_vo_invalid_member(mock_cookie, mock_request_1):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    perun_openapi.api.members_manager_api.MembersManagerApi.get_member_by_user = (
        MagicMock(
            side_effect=ApiException(
                http_resp=HttpResponse('"name":"MemberNotExistsException"')
            ),
        )
    )
    expected_error_message = '"name":"MemberNotExistsException"'

    with pytest.raises(ApiException) as error:
        adapter.get_member_status_by_user_and_vo(TEST_USER, TEST_VO)
        assert str(error.value.args) == expected_error_message


@patch(
    "perun.connector.perun_openapi.api.members_manager_api.MembersManagerApi"
    ".get_member_by_user"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_member_status_by_user_and_vo_invalid_status(mock_cookie, mock_request_1):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    invalid_status = "THIS_IS_NOT_A_VALID_STATUS"
    invalid_status_error_msg = f'"{invalid_status}" is not a valid state.'
    test_member_external_representation = {"id": 1, "status": invalid_status}

    perun_openapi.api.members_manager_api.MembersManagerApi.get_member_by_user = (
        MagicMock(
            return_value=(
                test_member_external_representation,
                200,
                RESPONSE_HEADER_COOKIE,
            )
        )
    )

    with pytest.raises(ValueError) as error:
        _ = adapter.get_member_status_by_user_and_vo(TEST_USER, TEST_VO)

        mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
        mock_cookie().write.assert_called_with(COOKIE)

        assert str(error.value.args[0]) == invalid_status_error_msg


@patch(
    "perun.connector.perun_openapi.api.members_manager_api.MembersManagerApi"
    ".get_member_by_user"
)
@patch(
    "perun.connector.perun_openapi.api.vos_manager_api.VosManagerApi"
    ".get_vo_by_short_name"
)
@patch("builtins.open", new_callable=mock_open)
def test_is_user_in_vo_valid_member(mock_cookie, mock_request_1, mock_request_2):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    valid_status_name = "VALID"
    test_valid_member_external_representation = {"id": 1, "status": valid_status_name}

    perun_openapi.api.vos_manager_api.VosManagerApi.get_vo_by_short_name = MagicMock(
        return_value=(TEST_VO, 200, RESPONSE_HEADER_COOKIE)
    )

    perun_openapi.api.members_manager_api.MembersManagerApi.get_member_by_user = (
        MagicMock(
            return_value=(
                test_valid_member_external_representation,
                200,
                RESPONSE_HEADER_COOKIE,
            )
        )
    )

    user_is_valid_member = adapter.is_user_in_vo_by_short_name(
        TEST_USER, TEST_VO.short_name
    )

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert user_is_valid_member


@patch(
    "perun.connector.perun_openapi.api.members_manager_api.MembersManagerApi"
    ".get_member_by_user"
)
@patch(
    "perun.connector.perun_openapi.api.vos_manager_api.VosManagerApi"
    ".get_vo_by_short_name"
)
@patch("builtins.open", new_callable=mock_open)
def test_is_user_in_vo_invalid_member(mock_cookie, mock_request_1, mock_request_2):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    invalid_status_name = "INVALID"
    test_valid_member_external_representation = {"id": 1, "status": invalid_status_name}

    perun_openapi.api.vos_manager_api.VosManagerApi.get_vo_by_short_name = MagicMock(
        return_value=(TEST_VO, 200, RESPONSE_HEADER_COOKIE)
    )

    perun_openapi.api.members_manager_api.MembersManagerApi.get_member_by_user = (
        MagicMock(
            return_value=(
                test_valid_member_external_representation,
                200,
                RESPONSE_HEADER_COOKIE,
            )
        )
    )

    user_is_valid_member = adapter.is_user_in_vo_by_short_name(
        TEST_USER, TEST_VO.short_name
    )

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert not user_is_valid_member


@patch(
    "perun.connector.perun_openapi.api.vos_manager_api.VosManagerApi"
    ".get_vo_by_short_name"
)
@patch("builtins.open", new_callable=mock_open)
def test_is_user_in_vo_non_existing_vo(mock_cookie, mock_request_1, caplog):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    perun_openapi.api.vos_manager_api.VosManagerApi.get_vo_by_short_name = MagicMock(
        side_effect=ApiException(
            http_resp=HttpResponse('"name":"VoNotExistsException"')
        ),
    )
    short_name_missing_msg = '"name":"VoNotExistsException"'

    with pytest.raises(Exception) as error:
        adapter.is_user_in_vo_by_short_name(TEST_USER, "non_existing_short_name")
        assert str(error.value.args[0]) == short_name_missing_msg


def test_is_user_in_vo_user_without_id():
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    user_without_id_msg = "User's ID is empty"
    user_without_id = User(None, "He, who shall not be named")

    with pytest.raises(ValueError) as error:
        _ = adapter.is_user_in_vo_by_short_name(user_without_id, "some short name")
        assert str(error.value.args[0]) == user_without_id_msg


def test_is_user_in_vo_no_short_name_given():
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    short_name_missing_msg = "VO short name is empty"
    missing_short_name = None

    with pytest.raises(ValueError) as error:
        _ = adapter.is_user_in_vo_by_short_name(TEST_USER, missing_short_name)
        assert str(error.value.args[0]) == short_name_missing_msg


@patch(
    "perun.connector.perun_openapi.api.members_manager_api.MembersManagerApi"
    ".get_member_by_user"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_member_by_user_existing_user(mock_cookie, mock_request_1):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    perun_openapi.api.members_manager_api.MembersManagerApi.get_member_by_user = (
        MagicMock(
            return_value=(
                TEST_MEMBER_EXTERNAL_REPRESENTATION,
                200,
                RESPONSE_HEADER_COOKIE,
            )
        )
    )

    result_member = adapter.get_member_by_user(TEST_USER, TEST_VO)

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result_member == TEST_MEMBER_INTERNAL_REPRESENTATION


@patch(
    "perun.connector.perun_openapi.api.members_manager_api.MembersManagerApi"
    ".get_member_by_user"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_member_by_user_user_not_not_found_ex(mock_cookie, mock_request_1, caplog):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    perun_openapi.api.members_manager_api.MembersManagerApi.get_member_by_user = (
        MagicMock(
            side_effect=ApiException(
                http_resp=HttpResponse('"name":"MemberNotExistsException"')
            ),
        )
    )
    short_name_missing_msg = '"name":"MemberNotExistsException"'

    with pytest.raises(Exception) as error:
        adapter.get_member_by_user(TEST_USER, TEST_VO)
        assert str(error.value.args[0]) == short_name_missing_msg


@patch(
    "perun.connector.perun_openapi.api.facilities_manager_api.FacilitiesManagerApi"
    ".get_assigned_resources_for_facility"
)
@patch(
    "perun.connector.perun_openapi.api.resources_manager_api.ResourcesManagerApi"
    ".get_assigned_groups"
)
@patch(
    "perun.connector.perun_openapi.api.attributes_manager_api.AttributesManagerApi"
    ".get_attribute"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_resource_capabilities(
    mock_cookie, mock_request_1, mock_request_2, mock_request_3
):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    group_without_resource = Group(-2, None, "", "", "", "")
    test_user_groups = [
        TEST_GROUP_INTERNAL_REPRESENTATION_1,
        TEST_GROUP_INTERNAL_REPRESENTATION_2,
        group_without_resource,
    ]

    resource_without_group = {"id": -1}
    resource_of_group_1 = {"id": test_user_groups[0].id}
    resource_of_group_2 = {"id": test_user_groups[1].id}
    test_resource_groups = [
        ([resource_of_group_1, resource_of_group_2], 200, RESPONSE_HEADER_COOKIE),
        ([resource_without_group], 200, RESPONSE_HEADER_COOKIE),
        ([], 200, RESPONSE_HEADER_COOKIE),
    ]

    test_facility_resources = [{"id": 5}, {"id": 6}, {"id": 7}]

    perun_openapi.api.facilities_manager_api.FacilitiesManagerApi.get_assigned_resources_for_facility = MagicMock(
        return_value=(test_facility_resources, 200, RESPONSE_HEADER_COOKIE)
    )

    perun_openapi.api.resources_manager_api.ResourcesManagerApi.get_assigned_groups = (
        MagicMock(side_effect=test_resource_groups)
    )

    resource_capabilities_of_groups = ["test capability 1", "test capability 2"]
    resource_capabilities_without_group = ["test capability 3"]
    absent_capabilities = None
    external_capabilities = [
        ({"value": resource_capabilities_of_groups}, 200, RESPONSE_HEADER_COOKIE),
        ({"value": resource_capabilities_without_group}, 200, RESPONSE_HEADER_COOKIE),
        ({"value": absent_capabilities}, 200, RESPONSE_HEADER_COOKIE),
    ]

    perun_openapi.api.attributes_manager_api.AttributesManagerApi.get_attribute = (
        MagicMock(side_effect=external_capabilities)
    )

    expected_capabilities = ["test capability 1", "test capability 2"]
    result_capabilities = adapter.get_resource_capabilities_by_facility(
        TEST_INTERNAL_FACILITY_1, test_user_groups
    )

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert sorted(result_capabilities) == sorted(expected_capabilities)


def test_get_resource_capabilities_no_input_facility():
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    result_capabilities = adapter.get_resource_capabilities_by_facility(None, [])
    assert result_capabilities == []


@patch(
    "perun.connector.perun_openapi.api.attributes_manager_api.AttributesManagerApi"
    ".get_attribute"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_facility_capabilities(mock_cookie, mock_request_1):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    facility_capabilities = {"value": ["test capability 1", "test capability 2"]}
    perun_openapi.api.attributes_manager_api.AttributesManagerApi.get_attribute = (
        MagicMock(return_value=(facility_capabilities, 200, RESPONSE_HEADER_COOKIE))
    )

    expected_capabilities = facility_capabilities["value"]
    result_capabilities = adapter.get_facility_capabilities_by_facility(
        TEST_INTERNAL_FACILITY_1
    )

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert sorted(result_capabilities) == sorted(expected_capabilities)


def test_get_facility_capabilities_no_input_facility():
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    result_capabilities = adapter.get_facility_capabilities_by_facility(None)
    assert result_capabilities == []


@patch(
    "perun.connector.perun_openapi.api.attributes_manager_api.AttributesManagerApi"
    ".get_user_attributes_by_names"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_user_attributes_multiple_attributes(mock_cookie, mock_request_1):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    test_user_attributes = get_entity_specific_attributes("user")
    attr_names = [attr.get("name") for attr in test_user_attributes]

    perun_openapi.api.attributes_manager_api.AttributesManagerApi.get_user_attributes_by_names = MagicMock(
        return_value=(test_user_attributes, 200, RESPONSE_HEADER_COOKIE)
    )

    expected_attributes = {
        attr.get("namespace") + ":" + attr.get("friendlyName"): attr.get("value")
        for attr in test_user_attributes
    }

    result_attributes = adapter.get_user_attributes(TEST_USER, attr_names)

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result_attributes == expected_attributes


@patch(
    "perun.connector.perun_openapi.api.attributes_manager_api.AttributesManagerApi"
    ".get_user_attributes_by_names"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_user_attributes_no_attributes(mock_cookie, mock_request_1):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())

    # default attribute is loa
    default_attr = {
        "id": 1,
        "name": "perunUserAttribute_loa",
        "namespace": "urn:perun:user:attribute-def:virt",
        "display_name": "display name for loa",
        "type": "some type",
        "value": "sample value",
        "friendlyName": "loa",
    }

    perun_openapi.api.attributes_manager_api.AttributesManagerApi.get_user_attributes_by_names = MagicMock(
        return_value=([default_attr], 200, RESPONSE_HEADER_COOKIE)
    )

    expected_attribute = {
        default_attr["namespace"] + ":" + default_attr["friendlyName"]: default_attr[
            "value"
        ]
    }

    result_attributes = adapter.get_user_attributes(TEST_USER, [])

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result_attributes == expected_attribute


@patch(
    "perun.connector.perun_openapi.api.attributes_manager_api.AttributesManagerApi"
    ".get_entityless_attributes_by_name"
)
@patch(
    "perun.connector.perun_openapi.api.attributes_manager_api.AttributesManagerApi"
    ".get_entityless_keys"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_entityless_attribute_valid_attribute(
    mock_cookie, mock_request_1, mock_request_2
):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    test_entityless_attrs = get_entity_specific_attributes("entityless")
    test_entityless_attr_name = (
        test_entityless_attrs[0].get("namespace")
        + ":"
        + test_entityless_attrs[0].get("friendlyName")
    )
    test_entityless_keys = ["entityless key 1", "entityless_key_2"]

    perun_openapi.api.attributes_manager_api.AttributesManagerApi.get_entityless_attributes_by_name = MagicMock(
        return_value=(test_entityless_attrs, 200, RESPONSE_HEADER_COOKIE)
    )

    perun_openapi.api.attributes_manager_api.AttributesManagerApi.get_entityless_keys = MagicMock(
        return_value=(test_entityless_keys, 200, RESPONSE_HEADER_COOKIE)
    )

    expected_attrs = {}
    for i in range(len(test_entityless_attrs)):
        expected_attrs[test_entityless_keys[i]] = test_entityless_attrs[i]["value"]
    result_attributes = adapter.get_entityless_attribute(test_entityless_attr_name)

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result_attributes == expected_attrs


@patch(
    "perun.connector.perun_openapi.api.attributes_manager_api.AttributesManagerApi"
    ".get_entityless_attributes_by_name"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_entityless_attribute_attr_id_missing(mock_cookie, mock_request_1):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    test_entityless_attr_name = "perunEntitylessAttribute_orgAups"

    test_entityless_attr_without_id = {
        "id": None,
        "name": "perunEntitylessAttribute_orgAups",
        "namespace": "urn:perun:entityless:attribute-def:def:orgAups",
        "display_name": "display name for org aups",
        "type": "some type",
        "value": "sample value",
        "friendlyName": "orgAups",
    }

    perun_openapi.api.attributes_manager_api.AttributesManagerApi.get_entityless_attributes_by_name = MagicMock(
        return_value=([test_entityless_attr_without_id], 200, RESPONSE_HEADER_COOKIE)
    )

    result_attributes = adapter.get_entityless_attribute(test_entityless_attr_name)

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result_attributes == {}


@patch(
    "perun.connector.perun_openapi.api.attributes_manager_api.AttributesManagerApi"
    ".get_vo_attributes_by_names"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_vo_attributes_single_attribute(mock_cookie, mock_request_1):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    test_vo_attributes = get_entity_specific_attributes("vo")
    attr_names = [attr.get("name") for attr in test_vo_attributes]

    perun_openapi.api.attributes_manager_api.AttributesManagerApi.get_vo_attributes_by_names = MagicMock(
        return_value=(test_vo_attributes, 200, RESPONSE_HEADER_COOKIE)
    )

    expected_attribute = {
        attr.get("namespace") + ":" + attr.get("friendlyName"): attr.get("value")
        for attr in test_vo_attributes
    }

    result_attribute = adapter.get_vo_attributes(TEST_VO, attr_names)

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result_attribute == expected_attribute


@patch(
    "perun.connector.perun_openapi.api.attributes_manager_api.AttributesManagerApi"
    ".get_vo_attributes_by_names"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_vo_attributes_no_attributes(mock_cookie, mock_request_1):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    # default attribute is id
    default_attr = {
        "id": 1,
        "name": "perunVoAttribute_id",
        "namespace": "urn:perun:vo:attribute-def:core",
        "display_name": "display name for loa",
        "type": "some type",
        "value": 10,
        "friendlyName": "id",
    }

    perun_openapi.api.attributes_manager_api.AttributesManagerApi.get_vo_attributes_by_names = MagicMock(
        return_value=([default_attr], 200, RESPONSE_HEADER_COOKIE)
    )

    expected_attribute = {
        default_attr["namespace"] + ":" + default_attr["friendlyName"]: default_attr[
            "value"
        ]
    }

    result_attribute = adapter.get_vo_attributes(TEST_VO, [])

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result_attribute == expected_attribute


@patch(
    "perun.connector.perun_openapi.api.attributes_manager_api.AttributesManagerApi"
    ".get_facility_attributes_by_names"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_facility_attribute_valid_attribute(mock_cookie, mock_request_1):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    test_facility_attribute = get_entity_specific_attributes("facility")[0]
    test_attr_name = (
        test_facility_attribute.get("namespace")
        + ":"
        + test_facility_attribute.get("friendlyName")
    )

    perun_openapi.api.attributes_manager_api.AttributesManagerApi.get_facility_attributes_by_names = MagicMock(
        return_value=([test_facility_attribute], 200, RESPONSE_HEADER_COOKIE)
    )

    expected_attribute = test_facility_attribute.get("value")
    result_attribute = adapter.get_facility_attributes(
        TEST_INTERNAL_FACILITY_1, [test_attr_name]
    )

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result_attribute[test_attr_name] == expected_attribute


def test_get_attributes_multiple_attributes():
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    test_perun_attrs = get_entity_specific_attributes("user")
    processed_attributes = copy.deepcopy(test_perun_attrs)

    expected_attributes = {
        attr.get("namespace") + ":" + attr.get("friendlyName"): attr["value"]
        for attr in processed_attributes
    }

    result_attributes = adapter._get_attributes(test_perun_attrs)
    assert result_attributes == expected_attributes


def test_get_attributes_empty_attributes():
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    result_attributes = adapter._get_attributes([])
    assert result_attributes == {}


@patch(
    "perun.connector.perun_openapi.api.groups_manager_api.GroupsManagerApi.get_groups_where_member_is_active"
)
@patch("builtins.open", new_callable=mock_open)
def test_get_groups_where_member_is_active_not_member(mock_cookie, mock_request_1):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    perun_openapi.api.groups_manager_api.GroupsManagerApi.get_groups_where_member_is_active = MagicMock(
        side_effect=ApiException(
            http_resp=HttpResponse('"name":"MemberNotExistsException"')
        ),
    )
    short_name_missing_msg = '"name":"MemberNotExistsException"'

    with pytest.raises(Exception) as error:
        adapter.get_groups_where_member_is_active(TEST_MEMBER_INTERNAL_REPRESENTATION)
        assert str(error.value.args[0]) == short_name_missing_msg


@patch(
    "perun.connector.perun_openapi.api.groups_manager_api.GroupsManagerApi.get_groups_where_member_is_active"
)
@patch(
    "perun.connector.perun_openapi.api.attributes_manager_api.AttributesManagerApi"
    ".get_attribute"
)
@patch("perun.connector.perun_openapi.api.vos_manager_api.VosManagerApi.get_vo_by_id")
@patch("builtins.open", new_callable=mock_open)
def test_get_groups_where_member_is_active(
    mock_cookie, mock_request_1, mock_request_2, mock_request_3
):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    perun_openapi.api.groups_manager_api.GroupsManagerApi.get_groups_where_member_is_active = MagicMock(
        return_value=(
            [
                TEST_GROUP_EXTERNAL_REPRESENTATION_1,
                TEST_GROUP_EXTERNAL_REPRESENTATION_2,
            ],
            200,
            RESPONSE_HEADER_COOKIE,
        )
    )

    perun_openapi.api.attributes_manager_api.AttributesManagerApi.get_attribute = (
        MagicMock(
            return_value=(
                {"value": SAMPLE_SHORT_GROUP_NAME},
                200,
                RESPONSE_HEADER_COOKIE,
            )
        )
    )

    perun_openapi.api.vos_manager_api.VosManagerApi.get_vo_by_id = MagicMock(
        return_value=(TEST_VO, 200, RESPONSE_HEADER_COOKIE)
    )

    result = adapter.get_groups_where_member_is_active(
        TEST_MEMBER_INTERNAL_REPRESENTATION
    )

    for group in result:
        assert isinstance(group, Group)

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert [
        TEST_GROUP_INTERNAL_REPRESENTATION_1,
        TEST_GROUP_INTERNAL_REPRESENTATION_2,
    ] == result


@patch(
    "perun.connector.perun_openapi.api.registrar_manager_api.RegistrarManagerApi.get_group_application_form"
)
@patch("builtins.open", new_callable=mock_open)
def test_has_registration_form_group(mock_cookie, mock_request_1):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    perun_openapi.api.registrar_manager_api.RegistrarManagerApi.get_group_application_form = MagicMock(
        return_value=("Application", 200, RESPONSE_HEADER_COOKIE)
    )

    result = adapter.has_registration_form_group(TEST_GROUP_INTERNAL_REPRESENTATION_1)

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result


@patch(
    "perun.connector.perun_openapi.api.registrar_manager_api.RegistrarManagerApi.get_group_application_form"
)
@patch("builtins.open", new_callable=mock_open)
def test_has_registration_form_group_no_form(mock_cookie, mock_request_1):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    perun_openapi.api.registrar_manager_api.RegistrarManagerApi.get_group_application_form = MagicMock(
        return_value=([], 200, RESPONSE_HEADER_COOKIE)
    )

    result = adapter.has_registration_form_group(TEST_GROUP_INTERNAL_REPRESENTATION_1)

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert not result


@patch(
    "perun.connector.perun_openapi.api.registrar_manager_api.RegistrarManagerApi.get_vo_application_form"
)
@patch("builtins.open", new_callable=mock_open)
def test_has_registration_form_vo(mock_cookie, mock_request_1):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    perun_openapi.api.registrar_manager_api.RegistrarManagerApi.get_vo_application_form = MagicMock(
        return_value=("Application", 200, RESPONSE_HEADER_COOKIE)
    )

    result = adapter.has_registration_form_vo(TEST_VO)

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert result


@patch(
    "perun.connector.perun_openapi.api.registrar_manager_api.RegistrarManagerApi.get_vo_application_form"
)
@patch("builtins.open", new_callable=mock_open)
def test_has_registration_form_vo_no_form(mock_cookie, mock_request_1):
    adapter = PerunRpcAdapter(CONFIG, ConfigStore.get_attribute_map())
    perun_openapi.api.registrar_manager_api.RegistrarManagerApi.get_vo_application_form = MagicMock(
        return_value=(None, 200, RESPONSE_HEADER_COOKIE)
    )

    result = adapter.has_registration_form_vo(TEST_VO)

    mock_cookie.assert_called_with(COOKIE_FILEPATH, "w")
    mock_cookie().write.assert_called_with(COOKIE)

    assert not result
