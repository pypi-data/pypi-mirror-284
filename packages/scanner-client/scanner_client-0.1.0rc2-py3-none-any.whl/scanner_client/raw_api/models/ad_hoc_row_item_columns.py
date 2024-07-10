from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="AdHocRowItemColumns")


@_attrs_define
class AdHocRowItemColumns:
    """ 
     """

    additional_properties: Dict[str, Union[None, float, str]] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            
            field_dict[prop_name] = prop

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ad_hoc_row_item_columns = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            def _parse_additional_property(data: object) -> Union[None, float, str]:
                if data is None:
                    return data
                return cast(Union[None, float, str], data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        ad_hoc_row_item_columns.additional_properties = additional_properties
        return ad_hoc_row_item_columns

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Union[None, float, str]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Union[None, float, str]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
