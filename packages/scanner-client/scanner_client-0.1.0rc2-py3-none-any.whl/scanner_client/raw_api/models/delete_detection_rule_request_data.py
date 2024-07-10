from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="DeleteDetectionRuleRequestData")


@_attrs_define
class DeleteDetectionRuleRequestData:
    """ 
        Attributes:
            id (str):
     """

    id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        delete_detection_rule_request_data = cls(
            id=id,
        )

        delete_detection_rule_request_data.additional_properties = d
        return delete_detection_rule_request_data

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
