from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, List
from ..models.rbac_detection_rule_permission_type import RbacDetectionRulePermissionType






T = TypeVar("T", bound="StartingPermissionsForRbacDetectionRulePermissionTypePermissionsByRole")


@_attrs_define
class StartingPermissionsForRbacDetectionRulePermissionTypePermissionsByRole:
    """ 
     """

    additional_properties: Dict[str, List[RbacDetectionRulePermissionType]] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for additional_property_item_data in prop:
                additional_property_item = additional_property_item_data.value
                field_dict[prop_name].append(additional_property_item)





        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        starting_permissions_for_rbac_detection_rule_permission_type_permissions_by_role = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for additional_property_item_data in (_additional_property):
                additional_property_item = RbacDetectionRulePermissionType(additional_property_item_data)



                additional_property.append(additional_property_item)

            additional_properties[prop_name] = additional_property

        starting_permissions_for_rbac_detection_rule_permission_type_permissions_by_role.additional_properties = additional_properties
        return starting_permissions_for_rbac_detection_rule_permission_type_permissions_by_role

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> List[RbacDetectionRulePermissionType]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: List[RbacDetectionRulePermissionType]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
