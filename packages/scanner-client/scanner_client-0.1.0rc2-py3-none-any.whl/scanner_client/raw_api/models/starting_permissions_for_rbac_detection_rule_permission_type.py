from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import cast

if TYPE_CHECKING:
  from ..models.starting_permissions_for_rbac_detection_rule_permission_type_permissions_by_role import StartingPermissionsForRbacDetectionRulePermissionTypePermissionsByRole





T = TypeVar("T", bound="StartingPermissionsForRbacDetectionRulePermissionType")


@_attrs_define
class StartingPermissionsForRbacDetectionRulePermissionType:
    """ Permissions to assign to newly-created resources

        Attributes:
            permissions_by_role (StartingPermissionsForRbacDetectionRulePermissionTypePermissionsByRole):
     """

    permissions_by_role: 'StartingPermissionsForRbacDetectionRulePermissionTypePermissionsByRole'
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.starting_permissions_for_rbac_detection_rule_permission_type_permissions_by_role import StartingPermissionsForRbacDetectionRulePermissionTypePermissionsByRole
        permissions_by_role = self.permissions_by_role.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "permissions_by_role": permissions_by_role,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.starting_permissions_for_rbac_detection_rule_permission_type_permissions_by_role import StartingPermissionsForRbacDetectionRulePermissionTypePermissionsByRole
        d = src_dict.copy()
        permissions_by_role = StartingPermissionsForRbacDetectionRulePermissionTypePermissionsByRole.from_dict(d.pop("permissions_by_role"))




        starting_permissions_for_rbac_detection_rule_permission_type = cls(
            permissions_by_role=permissions_by_role,
        )

        starting_permissions_for_rbac_detection_rule_permission_type.additional_properties = d
        return starting_permissions_for_rbac_detection_rule_permission_type

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
