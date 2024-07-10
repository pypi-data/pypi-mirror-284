from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="TinesConfiguration")


@_attrs_define
class TinesConfiguration:
    """ Represents Tines configuration, but only with fields that are safe to share in public, i.e. secrets info removed.

        Attributes:
            path (str):
            tines_tenant (str):
     """

    path: str
    tines_tenant: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        path = self.path

        tines_tenant = self.tines_tenant


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "path": path,
            "tines_tenant": tines_tenant,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path")

        tines_tenant = d.pop("tines_tenant")

        tines_configuration = cls(
            path=path,
            tines_tenant=tines_tenant,
        )

        tines_configuration.additional_properties = d
        return tines_configuration

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
