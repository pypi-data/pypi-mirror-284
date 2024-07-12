import re
from typing import List, Optional, Union

from perun.connector import perun_openapi
from perun.connector.adapters.AdapterInterface import AdapterInterface
from perun.connector.models.Facility import Facility
from perun.connector.models.Group import Group
from perun.connector.models.Member import Member
from perun.connector.models.MemberStatusEnum import MemberStatusEnum
from perun.connector.models.Resource import Resource
from perun.connector.models.User import User
from perun.connector.models.UserExtSource import UserExtSource
from perun.connector.models.VO import VO
from perun.connector.perun_openapi import ApiClient, Configuration
from perun.connector.perun_openapi.api.attributes_manager_api import (
    AttributesManagerApi,
)
from perun.connector.perun_openapi.api.authz_resolver_api import AuthzResolverApi
from perun.connector.perun_openapi.api.facilities_manager_api import (
    FacilitiesManagerApi,
)
from perun.connector.perun_openapi.api.groups_manager_api import GroupsManagerApi
from perun.connector.perun_openapi.api.members_manager_api import MembersManagerApi
from perun.connector.perun_openapi.api.registrar_manager_api import RegistrarManagerApi
from perun.connector.perun_openapi.api.resources_manager_api import ResourcesManagerApi
from perun.connector.perun_openapi.api.searcher_api import SearcherApi
from perun.connector.perun_openapi.api.users_manager_api import UsersManagerApi
from perun.connector.perun_openapi.api.vos_manager_api import VosManagerApi
from perun.connector.perun_openapi.exceptions import ApiException
from perun.connector.perun_openapi.model.attribute import Attribute
from perun.connector.perun_openapi.model.input_get_facilities import InputGetFacilities
from perun.connector.perun_openapi.model.input_set_facility_attributes import (
    InputSetFacilityAttributes,
)
from perun.connector.perun_openapi.model.input_set_user_attributes import (
    InputSetUserAttributes,
)
from perun.connector.perun_openapi.model.input_set_user_ext_source_attributes import (
    InputSetUserExtSourceAttributes,
)
from perun.connector.utils.AttributeUtils import AttributeUtils
from perun.connector.utils.Logger import Logger


class RPCAdapterNotExistsException(Exception):
    def __init__(self, message):
        self.body = message
        super().__init__(self.body)


class PerunRpcAdapter(AdapterInterface):
    def __init__(self, config_data: dict[str, str], attrs_map):
        self._CONFIG = None
        self._logger = Logger.get_logger(self.__class__.__name__)
        self._BASIC_AUTH = "BasicAuth"
        self._BEARER_AUTH = "BearerAuth"
        self._API_KEY_AUTH = "ApiKeyAuth"

        self._set_up_openapi_config(config_data)

        if "rp_id_attribute" not in config_data:
            self._RP_ID_ATTR = "urn:perun:facility:attribute-def:def:rpIdentifier"
        else:
            self._RP_ID_ATTR = config_data["rp_id_attribute"]

        self._ATTRIBUTE_UTILS = AttributeUtils(attrs_map)
        self._COOKIE_FILEPATH = config_data.get(
            "cookie_filepath", "/tmp/perun-cookie.txt"
        )
        self.cookie = self._load_cookie_from_file(self._COOKIE_FILEPATH)

    def _set_up_openapi_config(self, config_data: dict[str, str]) -> None:
        auth_type = config_data["auth_type"]
        self._CONFIG = Configuration(host=config_data["host"])

        if auth_type == self._BASIC_AUTH:
            self._CONFIG.username = config_data["username"]
            self._CONFIG.password = config_data["password"]
        elif auth_type == self._BEARER_AUTH:
            self._CONFIG.access_token = config_data["access_token"]
        elif auth_type == self._API_KEY_AUTH:
            self._CONFIG.api_key[self._API_KEY_AUTH] = config_data["api_key"]
        else:
            exception_message = (
                f'Authentication type "{auth_type}" is not a '
                f"supported way of authentication, please "
                f'set "auth_type" to one of "'
                f'{self._BASIC_AUTH}", "{self._BEARER_AUTH}" '
                f'or "{self._API_KEY_AUTH}"'
            )
            raise ValueError(exception_message)

    def _call_api(self, callable_method, params: dict):
        params["_return_http_data_only"] = False
        data, status, headers = callable_method(**params)
        cookie = headers.get("Set-Cookie", "")
        cookie = re.match(r"PERUNSESSION=\w+;", cookie)
        if cookie:
            cookie = cookie.group()
            if cookie != self.cookie:
                self.cookie = cookie
                self._save_cookie_to_file(self._COOKIE_FILEPATH, self.cookie)
        return data

    def get_perun_user(self, idp_id: str, uids: List[str]) -> Optional[User]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            api_instance = UsersManagerApi(api_client)
            for uid in uids:
                try:
                    user = self._call_api(
                        api_instance.get_user_by_ext_source_name_and_ext_login,
                        {"ext_login": uid, "ext_source_name": idp_id},
                    )
                    name = ""
                    for user_attr in [
                        "title_before",
                        "first_name",
                        "middle_name",
                        "last_name",
                        "title_after",
                    ]:
                        if user[user_attr] is not None:
                            name += user[user_attr] + " "

                    return User(user["id"], name.strip())
                except ApiException as ex:
                    if '"name":"UserExtSourceNotExistsException"' in ex.body:
                        continue
                    raise ex
        raise RPCAdapterNotExistsException(
            f"No user with uids '{str(uids)}' for idp: {idp_id} found."
        )

    def _get_group_unique_name(
        self,
        attributes_api_instance: AttributesManagerApi,
        group_name: str,
        group_id: int,
    ) -> str:
        attr = self._call_api(
            attributes_api_instance.get_attribute,
            {
                "group": group_id,
                "attribute_name": "urn:perun:group:attribute-def:virt:voShortName",
            },
        )
        return f'{attr["value"]}:{group_name}'

    def _create_internal_representation_groups(
        self,
        input_groups: List[perun_openapi.model.group.Group],
        converted_groups: List[Group],
        attributes_api_instance: AttributesManagerApi = None,
        vo: VO = None,
    ) -> None:
        unique_ids = []
        for group in input_groups:
            if group["id"] not in unique_ids:
                group["unique_name"] = (
                    ""
                    if not attributes_api_instance
                    else self._get_group_unique_name(
                        attributes_api_instance, group["name"], group["id"]
                    )
                )
                converted_groups.append(
                    Group(
                        group["id"],
                        vo if vo else self.get_vo(vo_id=group["vo_id"]),
                        group["uuid"],
                        group["name"],
                        group["unique_name"],
                        group["description"],
                    )
                )
                unique_ids.append(group["id"])

    def get_member_groups(
        self, user: Union[User, int], vo: Union[VO, int]
    ) -> List[Group]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            members_api_instance = MembersManagerApi(api_client)
            groups_api_instance = GroupsManagerApi(api_client)
            attributes_api_instance = AttributesManagerApi(api_client)

            converted_groups = []
            if not isinstance(vo, VO):
                vo = self.get_vo(vo_id=vo)
            user_id = AdapterInterface.get_object_id(user)
            member = self._call_api(
                members_api_instance.get_member_by_user, {"vo": vo.id, "user": user_id}
            )
            member_groups = []
            if member:
                member_groups = self._call_api(
                    groups_api_instance.get_all_member_groups, {"member": member["id"]}
                )
            self._create_internal_representation_groups(
                member_groups, converted_groups, attributes_api_instance, vo
            )
            return converted_groups

    def get_sp_groups_by_facility(self, facility: Union[Facility, int]) -> List[Group]:
        if facility is None:
            return []

        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            attributes_api_instance = AttributesManagerApi(api_client)
            facilities_api_instance = FacilitiesManagerApi(api_client)
            resources_api_instance = ResourcesManagerApi(api_client)

            facility_id = AdapterInterface.get_object_id(facility)
            resources = self._call_api(
                facilities_api_instance.get_assigned_resources_for_facility,
                {"facility": facility_id},
            )

            resources_ids = [resource.id for resource in resources]

            sp_groups = []
            for resource_id in resources_ids:
                groups = self._call_api(
                    resources_api_instance.get_assigned_groups,
                    {"resource": resource_id},
                )
                if groups:
                    vo = self.get_vo(vo_id=groups[0]["vo_id"])

                self._create_internal_representation_groups(
                    groups, sp_groups, attributes_api_instance, vo
                )
            return sp_groups

    def get_sp_groups_by_rp_id(self, rp_id: str) -> List[Group]:
        facility = self.get_facility_by_rp_identifier(rp_id)
        return self.get_sp_groups_by_facility(facility)

    def get_group_by_name(self, vo: Union[VO, int], name: str) -> Group:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            attributes_api_instance = AttributesManagerApi(api_client)
            groups_api_instance = GroupsManagerApi(api_client)

            vo_id = AdapterInterface.get_object_id(vo)
            group = self._call_api(
                groups_api_instance.get_group_by_name, {"vo": vo_id, "name": name}
            )
            group_external_representation = [group]
            converted_group = []
            self._create_internal_representation_groups(
                group_external_representation, converted_group, attributes_api_instance
            )
            return converted_group[0]

    def get_vo(self, short_name="", vo_id=None) -> Optional[VO]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            vos_api_instance = VosManagerApi(api_client)

            if short_name and vo_id:
                raise ValueError(
                    "VO can be obtained either by its short_name or id, "
                    "not both "
                    "at the same time."
                )
            elif vo_id:
                vo_lookup_method = vos_api_instance.get_vo_by_id
                vo_lookup_attribute = {"id": vo_id}
            elif short_name:
                vo_lookup_method = vos_api_instance.get_vo_by_short_name
                vo_lookup_attribute = {"short_name": short_name}
            else:
                raise ValueError(
                    "Neither short_name nor id was provided, please specify "
                    "exactly one to find VO by."
                )
            vo = self._call_api(vo_lookup_method, vo_lookup_attribute)
            return VO(vo.id, vo.name, vo.short_name)

    def get_facility_by_rp_identifier(self, rp_identifier: str) -> Optional[Facility]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            facilities_api_instance = FacilitiesManagerApi(api_client)

            facilities = self._call_api(
                facilities_api_instance.get_facilities_by_attribute,
                {"attribute_name": self._RP_ID_ATTR, "attribute_value": rp_identifier},
            )

            if not facilities:
                raise RPCAdapterNotExistsException(
                    f"No facility with rpID '{rp_identifier}' found."
                )

            if len(facilities) > 1:
                raise RPCAdapterNotExistsException(
                    f"There is more than one facility with rpID '{rp_identifier}'."
                )
            return Facility(
                facilities[0]["id"],
                facilities[0]["name"],
                facilities[0]["description"],
                rp_identifier,
                {},
            )

    def get_users_groups_on_facility(
        self, facility: Union[Facility, int], user: Union[User, int]
    ) -> List[Group]:
        if facility is None:
            return []

        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            users_api_instance = UsersManagerApi(api_client)
            attributes_api_instance = AttributesManagerApi(api_client)

            facility_id = AdapterInterface.get_object_id(facility)
            user_id = AdapterInterface.get_object_id(user)
            users_groups_on_facility = self._call_api(
                users_api_instance.get_groups_for_facility_where_user_is_active,
                {"user": user_id, "facility": facility_id},
            )
            converted_groups = []
            self._create_internal_representation_groups(
                users_groups_on_facility, converted_groups, attributes_api_instance
            )
            return converted_groups

    def get_users_groups_on_facility_by_rp_id(
        self, rp_identifier: str, user: Union[User, int]
    ) -> List[Group]:
        facility = self.get_facility_by_rp_identifier(rp_identifier)
        return self.get_users_groups_on_facility(facility, user)

    def _get_rp_id(self, facility: Union[Facility, int]) -> str:
        return self.get_facility_attributes(facility, [self._RP_ID_ATTR]).get(
            self._RP_ID_ATTR
        )

    def get_facilities_by_attribute_value(
        self, attribute: dict[str, str]
    ) -> List[Facility]:
        if len(attribute) != 1:
            self._logger.warning(
                f"Attribute must contain exactly one name and one value. "
                f'Given attribute contains: "{attribute}".'
            )
            return []

        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            searcher_api = SearcherApi(api_client)

            attribute_to_match_in_facilities = InputGetFacilities(attribute)
            perun_facilities = self._call_api(
                searcher_api.get_facilities,
                {"input_get_facilities": attribute_to_match_in_facilities},
            )

            facilities = []
            for perun_facility in perun_facilities:
                facility = Facility(
                    perun_facility["id"],
                    perun_facility["name"],
                    perun_facility["description"],
                    "",
                    {},
                )
                facility.rp_id = self._get_rp_id(facility)
                facilities.append(facility)

        return facilities

    def get_facility_attributes(
        self, facility: Union[Facility, int], attr_names: List[str]
    ) -> dict[str, Union[str, Optional[int], bool, List[str], dict[str, str]]]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            attributes_api_instance = AttributesManagerApi(api_client)

            facility_id = AdapterInterface.get_object_id(facility)
            perun_attrs = self._call_api(
                attributes_api_instance.get_facility_attributes_by_names,
                {"facility": facility_id, "attr_names": attr_names},
            )
            return self._get_attributes(perun_attrs)

    def get_user_ext_source(
        self, ext_source_name: str, ext_source_login: str
    ) -> UserExtSource:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            users_api_instance = UsersManagerApi(api_client)

            user_ext_source_perun = self._call_api(
                users_api_instance.get_user_ext_source_by_ext_login_and_ext_source_name,
                {
                    "ext_source_name": ext_source_name,
                    "ext_source_login": ext_source_login,
                },
            )

            ext_source_id = user_ext_source_perun["id"]
            login = user_ext_source_perun["login"]

            ext_source_details = user_ext_source_perun["ext_source"]
            name = ext_source_details["name"]

            user = self.get_perun_user(ext_source_name, [ext_source_login])

            return UserExtSource(ext_source_id, name, login, user)

    def get_user_ext_source_by_unique_attribute_value(
        self,
        attr_name: str,
        attr_value: Union[str, int, bool, List[str], dict[str, str]],
    ) -> UserExtSource:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            api_function = UsersManagerApi(
                api_client
            ).get_user_ext_source_by_unique_attribute_value_and_attribute_name

            try:
                user_ext_source_perun = self._call_api(
                    api_function,
                    {"attribute_name": attr_name, "attribute_value": attr_value},
                )
            except ApiException as ex:
                if '"name":"UserExtSourceNotExistsException"' in ex.body:
                    raise RPCAdapterNotExistsException(
                        f"No user ext source for attr name: '{attr_value}' value: "
                        f"{str(attr_value)} found."
                    )

            ext_source_id = user_ext_source_perun["id"]
            login = user_ext_source_perun["login"]

            ext_source_details = user_ext_source_perun["ext_source"]
            name = ext_source_details["name"]

            user = self.get_perun_user(name, [login])

            return UserExtSource(ext_source_id, name, login, user)

    def update_user_ext_source_last_access(
        self, user_ext_source: Union[UserExtSource, int]
    ) -> None:
        user_ext_source_id = AdapterInterface.get_object_id(user_ext_source)

        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            users_api_instance = UsersManagerApi(api_client)

            self._call_api(
                users_api_instance.update_user_ext_source_last_access,
                {"user_ext_source": user_ext_source_id},
            )

    def get_user_ext_source_attributes(
        self, user_ext_source: Union[UserExtSource, int], attr_names: List[str]
    ) -> dict[str, Union[str, Optional[int], bool, List[str], dict[str, str]]]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            attributes_api_instance = AttributesManagerApi(api_client)

            user_ext_source_id = AdapterInterface.get_object_id(user_ext_source)
            perun_attrs = self._call_api(
                attributes_api_instance.get_user_ext_source_attributes_by_names,
                {"user_ext_source": user_ext_source_id, "attr_names": attr_names},
            )
            return self._get_attributes(perun_attrs)

    def set_user_ext_source_attributes(
        self,
        user_ext_source: Union[UserExtSource, int],
        attributes: dict[
            str, Union[str, Optional[int], bool, List[str], dict[str, str]]
        ],
    ) -> None:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            attributes_api_instance = AttributesManagerApi(api_client)
            user_ext_source_id = AdapterInterface.get_object_id(user_ext_source)
            openapi_attributes = self.internal_to_open_api_attrs(attributes)
            input_arg = InputSetUserExtSourceAttributes(
                user_ext_source_id, openapi_attributes
            )
            self._call_api(
                attributes_api_instance.set_user_ext_source_attributes,
                {"input_set_user_ext_source_attributes": input_arg},
            )

    def set_user_attributes(
        self,
        user: Union[User, int],
        attributes: dict[
            str, Union[str, Optional[int], bool, List[str], dict[str, str]]
        ],
    ) -> None:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            attributes_api_instance = AttributesManagerApi(api_client)
            user_id = AdapterInterface.get_object_id(user)
            openapi_attributes = self.internal_to_open_api_attrs(attributes)
            input_arg = InputSetUserAttributes(user_id, openapi_attributes)
            self._call_api(
                attributes_api_instance.set_user_attributes,
                {"input_set_user_attributes": input_arg},
            )

    def internal_to_open_api_attrs(
        self,
        attributes: dict[
            str, Union[str, Optional[int], bool, List[str], dict[str, str]]
        ],
    ) -> List[Attribute]:
        attrs_cfg = self._ATTRIBUTE_UTILS.get_specific_attrs_config_dict(
            list(attributes.keys())
        )
        openapi_attributes = []
        for key, value in attrs_cfg.items():
            name_parts = key.split(":")
            namespace = ":".join(name_parts[:5])
            friendly_name = ":".join(name_parts[5:])
            openapi_attributes.append(
                Attribute(
                    id=value["id"],
                    bean_name="Attribute",
                    namespace=namespace,
                    friendly_name=friendly_name,
                    type=value["type"],
                    value=attributes[key],
                )
            )
        return openapi_attributes

    def get_member_status_by_user_and_vo(
        self, user: Union[User, int], vo: Union[VO, int]
    ) -> Optional[str]:
        member = self.get_member_by_user(user, vo)

        if member is not None:
            return member.status

        return None

    def is_user_in_vo_by_short_name(
        self, user: Union[User, int], vo_short_name: str
    ) -> bool:
        user_id = AdapterInterface.get_object_id(user)
        if not user_id:
            raise ValueError("User's ID is empty")

        if not vo_short_name:
            raise ValueError("VO short name is empty")

        vo_of_user = self.get_vo(short_name=vo_short_name)

        user_status = self.get_member_status_by_user_and_vo(user, vo_of_user)
        valid_status = MemberStatusEnum.VALID

        return user_status == valid_status

    def get_member_by_user(
        self, user: Union[User, int], vo: Union[VO, int]
    ) -> Optional[Member]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            members_api_instance = MembersManagerApi(api_client)

            user_id = AdapterInterface.get_object_id(user)
            vo_id = AdapterInterface.get_object_id(vo)

            member = self._call_api(
                members_api_instance.get_member_by_user, {"vo": vo_id, "user": user_id}
            )
            return Member(member["id"], vo, member["status"])

    def get_resource_capabilities_by_facility(
        self, facility: Union[Facility, int], user_groups: List[Union[Group, int]]
    ) -> List[str]:
        capabilities = []
        if facility is None:
            return capabilities

        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            facilities_api_instance = FacilitiesManagerApi(api_client)
            resources_api_instance = ResourcesManagerApi(api_client)
            attributes_api_instance = AttributesManagerApi(api_client)

            facility_id = AdapterInterface.get_object_id(facility)
            resources = self._call_api(
                facilities_api_instance.get_assigned_resources_for_facility,
                {"facility": facility_id},
            )
            user_groups_ids = [
                AdapterInterface.get_object_id(user_group) for user_group in user_groups
            ]
            for resource in resources:
                resource_groups = self._call_api(
                    resources_api_instance.get_assigned_groups,
                    {"resource": resource["id"]},
                )

                attr_name = "urn:perun:resource:attribute-def:def:capabilities"
                resource_capabilities = self._call_api(
                    attributes_api_instance.get_attribute,
                    {
                        "resource": resource["id"],
                        "attribute_name": attr_name,
                    },
                )["value"]

                if resource_capabilities is None:
                    continue

                for resource_group in resource_groups:
                    if resource_group["id"] in user_groups_ids:
                        capabilities.extend(resource_capabilities)
                        break
        return capabilities

    def get_resource_capabilities_by_rp_id(
        self, rp_identifier: str, user_groups: List[Union[Group, int]]
    ) -> List[str]:
        facility = self.get_facility_by_rp_identifier(rp_identifier)
        return self.get_resource_capabilities_by_facility(facility, user_groups)

    def get_facility_capabilities_by_facility(
        self, facility: Union[Facility, int]
    ) -> List[str]:
        if facility is None:
            return []

        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            attributes_api_instance = AttributesManagerApi(api_client)

            facility_id = AdapterInterface.get_object_id(facility)

            attr_name = "urn:perun:facility:attribute-def:def:capabilities"
            facility_capabilities = self._call_api(
                attributes_api_instance.get_attribute,
                {
                    "facility": facility_id,
                    "attribute_name": attr_name,
                },
            )["value"]

            return facility_capabilities

    def get_facility_capabilities_by_rp_id(self, rp_identifier: str) -> List[str]:
        facility = self.get_facility_by_rp_identifier(rp_identifier)
        return self.get_facility_capabilities_by_facility(facility)

    def get_resource_attributes(
        self, resource: Union[Resource, int], attr_names: List[str]
    ) -> dict[str, Union[str, Optional[int], bool, List[str], dict[str, str]]]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            attributes_api_instance = AttributesManagerApi(api_client)

            resource_id = AdapterInterface.get_object_id(resource)
            perun_attrs = self._call_api(
                attributes_api_instance.get_resource_attributes_by_names,
                {"resource": resource_id, "attr_names": attr_names},
            )
            return self._get_attributes(perun_attrs)

    def get_user_attributes(
        self, user: Union[User, int], attr_names: List[str]
    ) -> dict[str, Union[str, Optional[int], bool, List[str], dict[str, str]]]:
        default_attribute_name = "urn:perun:user:attribute-def:virt:loa"
        if not attr_names:
            attr_names.append(default_attribute_name)

        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            attributes_api_instance = AttributesManagerApi(api_client)
            user_id = AdapterInterface.get_object_id(user)

            perun_attrs = self._call_api(
                attributes_api_instance.get_user_attributes_by_names,
                {"user": user_id, "attr_names": attr_names},
            )

            return self._get_attributes(perun_attrs)

    def get_entityless_attribute(
        self, attr_name: str
    ) -> Union[str, Optional[int], bool, List[str], dict[str, str]]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            attributes_api_instance = AttributesManagerApi(api_client)

            attributes = {}
            perun_attr_values = self._call_api(
                attributes_api_instance.get_entityless_attributes_by_name,
                {"attr_name": attr_name},
            )

            attr_id = perun_attr_values[0].get("id")
            if attr_id is None:
                return attributes

            perun_attr_keys = self._call_api(
                attributes_api_instance.get_entityless_keys,
                {"attribute_definition": attr_id},
            )

            for i in range(len(perun_attr_values)):
                attributes[perun_attr_keys[i]] = perun_attr_values[i]["value"]
            return attributes

    def get_vo_attributes(
        self, vo: Union[VO, int], attr_names: List[str]
    ) -> dict[str, Union[str, Optional[int], bool, List[str], dict[str, str]]]:
        default_attribute_name = "urn:perun:vo:attribute-def:core:id"
        if not attr_names:
            attr_names.append(default_attribute_name)

        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            attributes_api_instance = AttributesManagerApi(api_client)

            vo_id = AdapterInterface.get_object_id(vo)

            perun_attrs = self._call_api(
                attributes_api_instance.get_vo_attributes_by_names,
                {"vo": vo_id, "attr_names": attr_names},
            )

            return self._get_attributes(perun_attrs)

    def _get_attributes(
        self,
        perun_attrs: List[dict[str, Union[str, int, bool, list[str], dict[str, str]]]],
    ) -> dict[str, Union[str, int, bool, list[str], dict[str, str]]]:
        attributes = {}
        for perun_attr in perun_attrs:
            perun_attr_name = perun_attr["namespace"] + ":" + perun_attr["friendlyName"]

            # for some reason open_api map int attributes as float
            if perun_attr["type"] == AttributeUtils.PERUN_INT:
                attributes[perun_attr_name] = int(perun_attr["value"])
            else:
                attributes[perun_attr_name] = perun_attr["value"]

        return attributes

    def get_groups_where_member_is_active(
        self, member: Union[Member, int]
    ) -> List[Group]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            member_id = self.get_object_id(member)
            internal_groups = []
            groups_api_instance = GroupsManagerApi(api_client)
            perun_groups = self._call_api(
                groups_api_instance.get_groups_where_member_is_active,
                {"member": member_id},
            )
            if isinstance(member, Member):
                vo = member.vo
            elif perun_groups:
                vo = self.get_vo(vo_id=perun_groups[0]["vo_id"])
            attributes_api_instance = AttributesManagerApi(api_client)
            self._create_internal_representation_groups(
                perun_groups, internal_groups, attributes_api_instance, vo
            )
            return internal_groups

    def get_groups_where_user_as_member_is_active(
        self, user: Union[User, int], vo: Union[VO, int]
    ) -> List[Group]:
        member = self.get_member_by_user(user, vo)
        return self.get_groups_where_member_is_active(member)

    def has_registration_form_group(self, group: Union[Group, int]) -> bool:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            group_id = self.get_object_id(group)
            registrar_api_instance = RegistrarManagerApi(api_client)
            if not self._call_api(
                registrar_api_instance.get_group_application_form, {"group": group_id}
            ):
                return False
            return True

    def has_registration_form_vo(self, vo: Union[VO, int]) -> bool:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            vo_id = self.get_object_id(vo)
            registrar_api_instance = RegistrarManagerApi(api_client)
            if not self._call_api(
                registrar_api_instance.get_vo_application_form, {"vo": vo_id}
            ):
                return False
            return True

    def has_registration_form_by_vo_short_name(self, vo_short_name: str) -> bool:
        vo = self.get_vo(vo_short_name)
        return self.has_registration_form_vo(vo)

    def create_facility(self, name: str, description="") -> Facility:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            facilities_api_instance = FacilitiesManagerApi(api_client)
            if description:
                return self._call_api(
                    facilities_api_instance.create_facility,
                    {"name": name, "description": description},
                )
            return self._call_api(
                facilities_api_instance.create_facility, {"name": name}
            )

    def set_facility_attributes(
        self,
        facility: Union[Facility, int],
        attributes: dict[
            str, Union[str, Optional[int], bool, List[str], dict[str, str]]
        ],
    ) -> None:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            attributes_api_instance = AttributesManagerApi(api_client)
            facility_id = AdapterInterface.get_object_id(facility)
            openapi_attributes = self.internal_to_open_api_attrs(attributes)

            self._call_api(
                attributes_api_instance.set_facility_attributes,
                {
                    "input_set_facility_attributes": InputSetFacilityAttributes(
                        facility=facility_id, attributes=openapi_attributes
                    )
                },
            )

    def get_attributes_definition(self) -> List[dict[str, Union[str, int, bool]]]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            attributes_api_instance = AttributesManagerApi(api_client)
            return self._call_api(
                attributes_api_instance.get_all_attribute_definitions, {}
            )

    def is_user_perun_admin(self, user: Union[User, int]) -> bool:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            authz_api_instance = AuthzResolverApi(api_client)
            if "perunadmin" in self._call_api(
                authz_api_instance.get_user_role_names,
                {"user": AdapterInterface.get_object_id(user)},
            ):
                return True
            return False

    def get_vos_where_user_is_admin(
        self, user: Union[User, int], check_perun_admin=True
    ) -> List[VO]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            if check_perun_admin and self.is_user_perun_admin(user):
                return self.get_all_vos()
            users_api_instance = UsersManagerApi(api_client)
            vos = self._call_api(
                users_api_instance.get_vos_where_user_is_admin,
                {"user": AdapterInterface.get_object_id(user)},
            )
            return [VO(vo.id, vo.name, vo.short_name) for vo in vos]

    def get_groups_where_user_is_admin(
        self,
        user: Union[User, int],
        check_perun_admin=True,
        fill_group_unique_name=True,
        fetch_related_vos=True,
    ) -> List[Group]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            if check_perun_admin and self.is_user_perun_admin(user):
                return self.get_all_groups(fetch_related_vos, fill_group_unique_name)
            else:
                users_api_instance = UsersManagerApi(api_client)
                groups = self._call_api(
                    users_api_instance.get_groups_where_user_is_admin,
                    {"user": AdapterInterface.get_object_id(user)},
                )
            return self._api_to_internal_groups(
                api_client, groups, fetch_related_vos, fill_group_unique_name
            )

    def get_facilities_where_user_is_admin(
        self, user: Union[User, int], check_perun_admin=True, fill_facility_rp_id=True
    ) -> List[Facility]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            if check_perun_admin and self.is_user_perun_admin(user):
                return self.get_all_facilities(fill_facility_rp_id)
            facilities_api_instance = FacilitiesManagerApi(api_client)
            facilities = self._call_api(
                facilities_api_instance.get_facilities_where_user_is_admin,
                {"user": AdapterInterface.get_object_id(user)},
            )
            return [
                Facility(
                    facility.id,
                    facility.name,
                    facility.description,
                    self._get_rp_id(facility.id) if fill_facility_rp_id else "",
                    {},
                )
                for facility in facilities
            ]

    def get_resources_where_user_is_admin(
        self,
        user: Union[User, int],
        check_perun_admin=True,
        fetch_related_vos=True,
        fetch_related_facilities=True,
        fill_facility_rp_id=True,
    ) -> List[Resource]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            resources_api_instance = ResourcesManagerApi(api_client)

            facilities = (
                self.get_all_facilities(fill_facility_rp_id)
                if fetch_related_facilities
                else []
            )
            vos = self.get_all_vos() if fetch_related_vos else []

            if check_perun_admin and self.is_user_perun_admin(user):
                resources = self._call_api(resources_api_instance.get_all_resources, {})
            else:
                resources = self._call_api(
                    resources_api_instance.get_all_resources_where_user_is_admin,
                    {"user": AdapterInterface.get_object_id(user)},
                )
            return [
                Resource(
                    resource.id,
                    self._find_vo_in_list_by_id(vos, resource.vo_id),
                    self._find_facility_in_list_by_id(facilities, resource.facility_id),
                    resource.name,
                )
                for resource in resources
            ]

    def get_all_vos(self) -> List[VO]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            vos_api_instance = VosManagerApi(api_client)
            vos = self._call_api(vos_api_instance.get_all_vos, {})
            return [VO(vo.id, vo.name, vo.short_name) for vo in vos]

    def get_all_facilities(self, fill_facility_rp_id=True) -> List[Facility]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            facilities_api_instance = FacilitiesManagerApi(api_client)
            facilities = self._call_api(facilities_api_instance.get_all_facilities, {})
            return [
                Facility(
                    facility.id,
                    facility.name,
                    facility.description,
                    "" if not fill_facility_rp_id else self._get_rp_id(facility.id),
                    {},
                )
                for facility in facilities
            ]

    def get_all_groups(
        self, fetch_related_vos=True, fill_group_unique_name=True
    ) -> List[Group]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            groups_api_instance = GroupsManagerApi(api_client)
            groups = self._call_api(groups_api_instance.get_all_groups_from_all_vos, {})
            return self._api_to_internal_groups(
                api_client, groups, fetch_related_vos, fill_group_unique_name
            )

    def get_all_resources(
        self,
        fetch_related_vos=True,
        fetch_related_facilities=True,
        fill_facility_rp_id=True,
    ) -> List[Resource]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            resources_api_instance = ResourcesManagerApi(api_client)
            resources = self._call_api(resources_api_instance.get_all_resources, {})
            return self._api_to_internal_resource(
                resources,
                fetch_related_vos,
                fetch_related_facilities,
                fill_facility_rp_id,
            )

    def get_groups_where_user_is_active_resource(
        self,
        user: Union[User, int],
        resource: Union[Resource, int],
        map_unique_name=True,
    ) -> List[Group]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            vo = None
            if isinstance(resource, Resource):
                vo = resource.vo
                resource_id = resource.id
            else:
                resource_id = resource

            if not vo:
                perun_vo = self._call_api(
                    ResourcesManagerApi(api_client).get_vo,
                    {"resource": resource_id},
                )
                vo = VO(perun_vo.id, perun_vo.name, perun_vo.short_name)

            result = []
            perun_groups = UsersManagerApi(
                api_client
            ).get_groups_for_resource_where_user_is_active(
                self.get_object_id(user), resource_id
            )
            self._create_internal_representation_groups(
                perun_groups,
                result,
                AttributesManagerApi(api_client) if map_unique_name else "",
                vo=vo,
            )
            return result

    def get_facility_by_id(self, facility_id: int) -> Facility:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            facility = self._call_api(
                FacilitiesManagerApi(api_client).get_facility_by_id, {"id": facility_id}
            )
            return Facility(
                facility_id,
                facility.name,
                facility.description,
                self._get_rp_id(facility_id),
                {},
            )

    def get_resources_for_facility(
        self, facility: Union[Facility, int], map_vo=True
    ) -> List[Resource]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            if isinstance(facility, Facility):
                facility_id = facility.id
            else:
                facility_id = facility
                facility = self.get_facility_by_id(facility)

            resources = self._call_api(
                FacilitiesManagerApi(api_client).get_assigned_resources_for_facility,
                {"facility": facility_id},
            )
            return [
                Resource(
                    resource.id,
                    self.get_vo(vo_id=resource.vo_id)
                    if map_vo
                    else VO(resource.vo_id, "", ""),
                    facility,
                    resource.name,
                )
                for resource in resources
            ]

    def get_group_ids_for_resource(self, resource: Union[Resource, int]) -> List[int]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            resource_id = self.get_object_id(resource)
            groups = self._call_api(
                ResourcesManagerApi(api_client).get_assigned_groups,
                {"resource": resource_id},
            )
            result = set()
            for group in groups:
                result.add(group["id"])
            return list(result)

    def get_groups_for_resource(
        self, resource: Union[Resource, int], map_unique_name=True
    ) -> List[Group]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            if isinstance(resource, Resource):
                resource_id = resource.id
            else:
                resource_id = resource
                resource = self.get_resource_by_id(resource_id)
            groups = self._call_api(
                ResourcesManagerApi(api_client).get_assigned_groups,
                {"resource": resource_id},
            )
            result = []
            self._create_internal_representation_groups(
                groups,
                result,
                AttributesManagerApi(api_client) if map_unique_name else "",
                vo=resource.vo,
            )
            return result

    def get_resource_by_id(
        self, resource_id: int, map_vo=True, map_facility=True
    ) -> Resource:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            resource = self._call_api(
                ResourcesManagerApi(api_client).get_resource_by_id, {"id": resource_id}
            )
            facility = (
                self.get_facility_by_id(resource.facility_id)
                if map_facility
                else Facility(resource.facility_id, "", "", "", {})
            )
            vo = (
                self.get_vo(vo_id=resource.vo_id)
                if map_vo
                else VO(resource.vo_id, "", "")
            )
            return Resource(resource.id, vo, facility, resource.name)

    def get_all_parent_groups_for_group(
        self, group: Union[Group, int], map_unique_name=True
    ) -> List[Group]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            perun_parent_groups = []
            perun_group = self._call_api(
                GroupsManagerApi(api_client).get_group_by_id,
                {"id": self.get_object_id(group)},
            )
            if isinstance(group, Group):
                vo = group.vo
            else:
                vo = self.get_vo(vo_id=perun_group.vo_id)
            if not perun_group.parent_group_id:
                return perun_parent_groups

            while perun_group.parent_group_id:
                perun_group = self._call_api(
                    GroupsManagerApi(api_client).get_parent_group,
                    {"group": perun_group.id},
                )
                perun_parent_groups.append(perun_group)
            result = []
            self._create_internal_representation_groups(
                perun_parent_groups,
                result,
                AttributesManagerApi(api_client) if map_unique_name else "",
                vo=vo,
            )
            return result

    def get_facilities_by_attribute_with_attributes(
        self,
        attr_name: str,
        attr_value: Union[str, int, bool, List[str], dict[str, str]],
        attr_names: List[str],
    ) -> List[Facility]:
        with ApiClient(self._CONFIG, cookie=self.cookie) as api_client:
            if self._RP_ID_ATTR not in attr_name:
                attr_names.append(self._RP_ID_ATTR)

            perun_facilities_attributes = self._call_api(
                FacilitiesManagerApi(
                    api_client
                ).get_facilities_by_attribute_with_attributes,
                {
                    "attribute_name": attr_name,
                    "attribute_value": attr_value,
                    "attr_names": attr_names,
                },
            )

            facilities = []
            for facility_attrs in perun_facilities_attributes:
                perun_facility = facility_attrs["facility"]
                attrs = self._get_attributes(facility_attrs["attributes"])
                facilities.append(
                    Facility(
                        perun_facility.id,
                        perun_facility.name,
                        perun_facility.description,
                        attrs[self._RP_ID_ATTR],
                        attrs,
                    )
                )
            return facilities

    def _save_cookie_to_file(self, filepath, cookie):
        with open(filepath, "w") as file:
            try:
                file.write(cookie)
            except OSError as e:
                self._logger(
                    f"Cannot write cookie to file: {filepath}, error: {e.strerror}"
                )

    def _api_to_internal_groups(
        self,
        api_client,
        api_groups,
        fetch_related_vos=True,
        fill_group_unique_name=True,
    ) -> List[Group]:
        vos = self.get_all_vos() if fetch_related_vos else []
        attributes_api_instance = AttributesManagerApi(api_client)
        return [
            Group(
                group.id,
                self._find_vo_in_list_by_id(vos, group.vo_id),
                group.uuid,
                group.name,
                ""
                if not fill_group_unique_name
                else self._get_group_unique_name(
                    attributes_api_instance, group.name, group.id
                ),
                group.description,
            )
            for group in api_groups
        ]

    def _api_to_internal_resource(
        self,
        api_resources,
        fetch_related_vos=True,
        fetch_related_facilities=True,
        fill_facility_rp_id=True,
    ) -> List[Resource]:
        facilities = (
            self.get_all_facilities(fill_facility_rp_id)
            if fetch_related_facilities
            else []
        )
        vos = self.get_all_vos() if fetch_related_vos else []
        return [
            Resource(
                resource.id,
                self._find_vo_in_list_by_id(vos, resource.vo_id),
                self._find_facility_in_list_by_id(facilities, resource.facility_id),
                resource.name,
            )
            for resource in api_resources
        ]

    @staticmethod
    def _find_vo_in_list_by_id(vo_list, vo_id):
        for vo in vo_list:
            if vo.id == vo_id:
                return vo
        return None

    @staticmethod
    def _find_facility_in_list_by_id(facility_list, facility_id):
        for facility in facility_list:
            if facility.id == facility_id:
                return facility
        return None

    @staticmethod
    def _load_cookie_from_file(filepath):
        try:
            with open(filepath, "r") as f:
                return f.read()
        except OSError:
            return None
