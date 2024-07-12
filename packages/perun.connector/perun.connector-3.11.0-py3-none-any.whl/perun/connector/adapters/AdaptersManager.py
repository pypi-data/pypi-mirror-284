import inspect
from typing import List, Optional, Union

from ldap3.core.exceptions import LDAPException

from perun.connector.adapters.AdapterInterface import AdapterInterface
from perun.connector.adapters.LdapAdapter import (
    AdapterSkipException,
    LdapAdapter,
    LDAPNotExistsException,
)
from perun.connector.adapters.PerunRpcAdapter import (
    PerunRpcAdapter,
    RPCAdapterNotExistsException,
)
from perun.connector.models.Facility import Facility
from perun.connector.models.Group import Group
from perun.connector.models.Member import Member
from perun.connector.models.Resource import Resource
from perun.connector.models.User import User
from perun.connector.models.UserExtSource import UserExtSource
from perun.connector.models.VO import VO
from perun.connector.perun_openapi import ApiException
from perun.connector.perun_openapi.exceptions import NotFoundException
from perun.connector.utils.Logger import Logger


class AdaptersManagerException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class AdaptersManagerNotExistsException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class AdaptersManager(AdapterInterface):
    def __init__(self, config, attrs_map):
        self._logger = Logger.get_logger(self.__class__.__name__)
        self._STARTING_PRIORITY = 1
        self.adapters = {}

        adapters_info = config["adapters"]

        for adapter_info in adapters_info:
            config_data = adapter_info.copy()
            adapter_type = config_data.pop("type")
            priority = config_data.pop("priority")

            if adapter_type == "ldap":
                ldap_adapter = LdapAdapter(config_data, attrs_map)

                self.adapters[priority] = {
                    "name": "ldap_adapter",
                    "adapter": ldap_adapter,
                }
            elif adapter_type == "openApi":
                rpc_adapter = PerunRpcAdapter(config_data, attrs_map)

                self.adapters[priority] = {
                    "name": "rpc_adapter",
                    "adapter": rpc_adapter,
                }
            else:
                self._logger.warning(
                    f'Config file includes unsupported adapter type "'
                    f'{adapter_type}"'
                )

    def _execute_method_by_priority(self, method_name: str, *args):
        current_priority = self._STARTING_PRIORITY
        current_adapter = self.adapters.get(current_priority)

        while current_adapter is not None:
            adapter_impl = current_adapter["adapter"]
            try:
                return getattr(adapter_impl, method_name)(*args)
            except AdapterSkipException as e:
                self._logger.warning(
                    f'{e.message} Method: "{method_name}" Adapter: '
                    f'{current_adapter["name"]} Going to try another '
                    f"adapter if available."
                )
                current_priority += 1
                current_adapter = self.adapters.get(current_priority)
            except (ApiException, LDAPException) as ex:
                if (ex.body and "NotExistsException" in ex.body) or isinstance(
                    ex, NotFoundException
                ):
                    raise AdaptersManagerNotExistsException(ex.body)
                self._logger.warning(
                    f'Method "{method_name}" could not be executed '
                    f'successfully by {current_adapter["name"]}, exception '
                    f'occurred: "{ex}" Going to try another '
                    f"adapter if available."
                )
                current_priority += 1
                current_adapter = self.adapters.get(current_priority)
            except (LDAPNotExistsException, RPCAdapterNotExistsException) as ex:
                raise AdaptersManagerNotExistsException(ex.body)

        raise AdaptersManagerException(
            f'None of the provided adapters was able to resolve method "'
            f'{method_name}"'
        )

    def _get_caller_name(self):
        return inspect.stack()[1].function

    def get_perun_user(self, idp_id: str, uids: List[str]) -> Optional[User]:
        return self._execute_method_by_priority(self._get_caller_name(), idp_id, uids)

    def get_group_by_name(self, vo: Union[int, VO], name: str) -> Group:
        return self._execute_method_by_priority(self._get_caller_name(), vo, name)

    def get_vo(self, short_name="", vo_id=None) -> VO:
        return self._execute_method_by_priority(
            self._get_caller_name(), short_name, vo_id
        )

    def get_member_groups(
        self, user: Union[int, User], vo: Union[int, VO]
    ) -> List[Group]:
        return self._execute_method_by_priority(self._get_caller_name(), user, vo)

    def get_sp_groups_by_facility(self, facility: Union[Facility, int]) -> List[Group]:
        return self._execute_method_by_priority(self._get_caller_name(), facility)

    def get_sp_groups_by_rp_id(self, rp_id: str) -> List[Group]:
        return self._execute_method_by_priority(self._get_caller_name(), rp_id)

    def get_resource_attributes(
        self, resource: Union[int, Resource], attr_names: List[str]
    ) -> dict[str, Union[str, Optional[int], bool, List[str], dict[str, str]]]:
        return self._execute_method_by_priority(
            self._get_caller_name(), resource, attr_names
        )

    def get_user_attributes(
        self, user: Union[int, User], attr_names: List[str]
    ) -> dict[str, Union[str, Optional[int], bool, List[str], dict[str, str]]]:
        return self._execute_method_by_priority(
            self._get_caller_name(), user, attr_names
        )

    def get_entityless_attribute(
        self, attr_name: str
    ) -> Union[str, Optional[int], bool, List[str], dict[str, str]]:
        return self._execute_method_by_priority(self._get_caller_name(), attr_name)

    def get_vo_attributes(
        self, vo: Union[int, VO], attr_names: List[str]
    ) -> dict[str, Union[str, Optional[int], bool, List[str], dict[str, str]]]:
        return self._execute_method_by_priority(self._get_caller_name(), vo, attr_names)

    def get_facility_by_rp_identifier(self, rp_identifier: str) -> Facility:
        return self._execute_method_by_priority(self._get_caller_name(), rp_identifier)

    def get_users_groups_on_facility_by_rp_id(
        self, rp_identifier: str, user: Union[User, int]
    ) -> List[Group]:
        return self._execute_method_by_priority(
            self._get_caller_name(), rp_identifier, user
        )

    def get_users_groups_on_facility(
        self, facility: Union[Facility, int], user: Union[User, int]
    ) -> List[Group]:
        return self._execute_method_by_priority(self._get_caller_name(), facility, user)

    def get_facilities_by_attribute_value(
        self, attribute: dict[str, str]
    ) -> List[Facility]:
        return self._execute_method_by_priority(self._get_caller_name(), attribute)

    def get_facility_attributes(
        self, facility: Union[int, Facility], attr_names: List[str]
    ) -> dict[str, Union[str, Optional[int], bool, List[str], dict[str, str]]]:
        return self._execute_method_by_priority(
            self._get_caller_name(), facility, attr_names
        )

    def get_user_ext_source(
        self, ext_source_name: str, ext_source_login: str
    ) -> UserExtSource:
        return self._execute_method_by_priority(
            self._get_caller_name(), ext_source_name, ext_source_login
        )

    def get_user_ext_source_by_unique_attribute_value(
        self,
        attr_name: str,
        attr_value: Union[str, int, bool, List[str], dict[str, str]],
    ) -> UserExtSource:
        return self._execute_method_by_priority(
            self._get_caller_name(), attr_name, attr_value
        )

    def update_user_ext_source_last_access(self, user_ext_source: str) -> None:
        return self._execute_method_by_priority(
            self._get_caller_name(), user_ext_source
        )

    def get_user_ext_source_attributes(
        self, user_ext_source: Union[int, UserExtSource], attr_names: List[str]
    ) -> dict[str, Union[str, Optional[int], bool, List[str], dict[str, str]]]:
        return self._execute_method_by_priority(
            self._get_caller_name(), user_ext_source, attr_names
        )

    def set_user_ext_source_attributes(
        self,
        user_ext_source: Union[int, UserExtSource],
        attributes: dict[
            str, Union[str, Optional[int], bool, List[str], dict[str, str]]
        ],
    ) -> None:
        return self._execute_method_by_priority(
            self._get_caller_name(), user_ext_source, attributes
        )

    def set_user_attributes(
        self,
        user: Union[User, int],
        attributes: dict[
            str, Union[str, Optional[int], bool, List[str], dict[str, str]]
        ],
    ) -> None:
        return self._execute_method_by_priority(
            self._get_caller_name(), user, attributes
        )

    def get_member_status_by_user_and_vo(
        self, user: Union[int, User], vo: Union[int, VO]
    ) -> str:
        return self._execute_method_by_priority(self._get_caller_name(), user, vo)

    def is_user_in_vo_by_short_name(
        self, user: Union[int, User], vo_short_name: str
    ) -> bool:
        return self._execute_method_by_priority(
            self._get_caller_name(), user, vo_short_name
        )

    def get_resource_capabilities_by_facility(
        self, facility: Union[Facility, int], user_groups: List[Union[Group, int]]
    ) -> List[str]:
        return self._execute_method_by_priority(
            self._get_caller_name(), facility, user_groups
        )

    def get_resource_capabilities_by_rp_id(
        self, rp_identifier: str, user_groups: List[Union[Group, int]]
    ) -> List[str]:
        return self._execute_method_by_priority(
            self._get_caller_name(), rp_identifier, user_groups
        )

    def get_facility_capabilities_by_rp_id(self, rp_identifier: str) -> List[str]:
        return self._execute_method_by_priority(self._get_caller_name(), rp_identifier)

    def get_facility_capabilities_by_facility(
        self, facility: Union[Facility, int]
    ) -> List[str]:
        return self._execute_method_by_priority(self._get_caller_name(), facility)

    def get_groups_where_member_is_active(
        self, member: Union[Member, int]
    ) -> List[Group]:
        return self._execute_method_by_priority(self._get_caller_name(), member)

    def get_groups_where_user_as_member_is_active(
        self, user: Union[User, int], vo: Union[VO, int]
    ) -> List[Group]:
        return self._execute_method_by_priority(self._get_caller_name(), user, vo)

    def has_registration_form_group(self, group: Union[Group, int]) -> bool:
        return self._execute_method_by_priority(self._get_caller_name(), group)

    def has_registration_form_vo(self, vo: Union[VO, int]) -> bool:
        return self._execute_method_by_priority(self._get_caller_name(), vo)

    def has_registration_form_by_vo_short_name(self, vo_short_name: str) -> bool:
        return self._execute_method_by_priority(self._get_caller_name(), vo_short_name)

    def create_facility(self, name: str, description="") -> Facility:
        return self._execute_method_by_priority(
            self._get_caller_name(), name, description
        )

    def set_facility_attributes(
        self,
        facility: Union[Facility, int],
        attributes: dict[
            str, Union[str, Optional[int], bool, List[str], dict[str, str]]
        ],
    ) -> None:
        return self._execute_method_by_priority(
            self._get_caller_name(), facility, attributes
        )

    def get_attributes_definition(self) -> List[dict[str, Union[str, int, bool]]]:
        return self._execute_method_by_priority(self._get_caller_name())

    def get_member_by_user(
        self, user: Union[User, int], vo: Union[VO, int]
    ) -> Optional[Member]:
        return self._execute_method_by_priority(self._get_caller_name(), user, vo)

    def is_user_perun_admin(self, user: Union[User, int]) -> bool:
        return self._execute_method_by_priority(self._get_caller_name(), user)

    def get_vos_where_user_is_admin(
        self, user: Union[User, int], check_perun_admin=True
    ) -> List[VO]:
        return self._execute_method_by_priority(
            self._get_caller_name(), user, check_perun_admin
        )

    def get_groups_where_user_is_admin(
        self,
        user: Union[User, int],
        check_perun_admin=True,
        fill_group_unique_name=True,
        fetch_related_vos=True,
    ) -> List[Group]:
        return self._execute_method_by_priority(
            self._get_caller_name(),
            user,
            check_perun_admin,
            fill_group_unique_name,
            fetch_related_vos,
        )

    def get_facilities_where_user_is_admin(
        self, user: Union[User, int], check_perun_admin=True, fill_facility_rp_id=True
    ) -> List[Facility]:
        return self._execute_method_by_priority(
            self._get_caller_name(), user, check_perun_admin, fill_facility_rp_id
        )

    def get_resources_where_user_is_admin(
        self,
        user: Union[User, int],
        check_perun_admin=True,
        fetch_related_vos=True,
        fetch_related_facilities=True,
        fill_facility_rp_id=True,
    ) -> List[Resource]:
        return self._execute_method_by_priority(
            self._get_caller_name(),
            user,
            check_perun_admin,
            fetch_related_vos,
            fetch_related_facilities,
            fill_facility_rp_id,
        )

    def get_all_vos(self) -> List[VO]:
        return self._execute_method_by_priority(self._get_caller_name())

    def get_all_facilities(self, fill_facility_rp_id=True) -> List[Facility]:
        return self._execute_method_by_priority(
            self._get_caller_name(), fill_facility_rp_id
        )

    def get_all_groups(
        self, fetch_related_vos=True, fill_group_unique_name=True
    ) -> List[Group]:
        return self._execute_method_by_priority(
            self._get_caller_name(), fetch_related_vos, fill_group_unique_name
        )

    def get_all_resources(
        self,
        fetch_related_vos=True,
        fetch_related_facilities=True,
        fill_facility_rp_id=True,
    ) -> List[Resource]:
        return self._execute_method_by_priority(
            self._get_caller_name(),
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
        return self._execute_method_by_priority(
            self._get_caller_name(), user, resource, map_unique_name
        )

    def get_facility_by_id(self, facility_id: int) -> Facility:
        return self._execute_method_by_priority(self._get_caller_name(), facility_id)

    def get_resources_for_facility(
        self, facility: Union[Facility, int], map_vo=True
    ) -> List[Resource]:
        return self._execute_method_by_priority(
            self._get_caller_name(), facility, map_vo
        )

    def get_group_ids_for_resource(self, resource: Union[Resource, int]) -> List[int]:
        return self._execute_method_by_priority(self._get_caller_name(), resource)

    def get_groups_for_resource(
        self, resource: Union[Resource, int], map_unique_name=True
    ) -> List[Group]:
        return self._execute_method_by_priority(
            self._get_caller_name(), resource, map_unique_name
        )

    def get_resource_by_id(
        self, resource_id: int, map_vo=True, map_facility=True
    ) -> Resource:
        return self._execute_method_by_priority(
            self._get_caller_name(), resource_id, map_vo, map_facility
        )

    def get_all_parent_groups_for_group(
        self, group: Union[Group, int], map_unique_name=True
    ) -> List[Group]:
        return self._execute_method_by_priority(
            self._get_caller_name(), group, map_unique_name
        )

    def get_facilities_by_attribute_with_attributes(
        self,
        attr_name: str,
        attr_value: Union[str, int, bool, List[str], dict[str, str]],
        attr_names: List[str],
    ) -> List[Facility]:
        return self._execute_method_by_priority(
            self._get_caller_name(), attr_name, attr_value, attr_names
        )
