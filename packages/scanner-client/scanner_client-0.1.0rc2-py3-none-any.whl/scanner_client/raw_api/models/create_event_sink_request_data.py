from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union
from typing import Dict
from typing import cast

if TYPE_CHECKING:
  from ..models.create_event_sink_args_type_1 import CreateEventSinkArgsType1
  from ..models.create_event_sink_args_type_0 import CreateEventSinkArgsType0





T = TypeVar("T", bound="CreateEventSinkRequestData")


@_attrs_define
class CreateEventSinkRequestData:
    """ 
        Attributes:
            description (str):
            event_sink_args (Union['CreateEventSinkArgsType0', 'CreateEventSinkArgsType1']):
            name (str):
            tenant_id (str):
     """

    description: str
    event_sink_args: Union['CreateEventSinkArgsType0', 'CreateEventSinkArgsType1']
    name: str
    tenant_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.create_event_sink_args_type_1 import CreateEventSinkArgsType1
        from ..models.create_event_sink_args_type_0 import CreateEventSinkArgsType0
        description = self.description

        event_sink_args: Dict[str, Any]
        if isinstance(self.event_sink_args, CreateEventSinkArgsType0):
            event_sink_args = self.event_sink_args.to_dict()
        else:
            event_sink_args = self.event_sink_args.to_dict()


        name = self.name

        tenant_id = self.tenant_id


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "description": description,
            "event_sink_args": event_sink_args,
            "name": name,
            "tenant_id": tenant_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_event_sink_args_type_1 import CreateEventSinkArgsType1
        from ..models.create_event_sink_args_type_0 import CreateEventSinkArgsType0
        d = src_dict.copy()
        description = d.pop("description")

        def _parse_event_sink_args(data: object) -> Union['CreateEventSinkArgsType0', 'CreateEventSinkArgsType1']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_create_event_sink_args_type_0 = CreateEventSinkArgsType0.from_dict(data)



                return componentsschemas_create_event_sink_args_type_0
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_create_event_sink_args_type_1 = CreateEventSinkArgsType1.from_dict(data)



            return componentsschemas_create_event_sink_args_type_1

        event_sink_args = _parse_event_sink_args(d.pop("event_sink_args"))


        name = d.pop("name")

        tenant_id = d.pop("tenant_id")

        create_event_sink_request_data = cls(
            description=description,
            event_sink_args=event_sink_args,
            name=name,
            tenant_id=tenant_id,
        )

        create_event_sink_request_data.additional_properties = d
        return create_event_sink_request_data

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
