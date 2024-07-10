from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

import datetime
from dateutil.parser import isoparse
from ..models.event_sink_type import EventSinkType
from typing import Dict
from ..models.event_sink_configuration_type_0 import EventSinkConfigurationType0
from typing import cast, Union
from typing import cast

if TYPE_CHECKING:
  from ..models.event_sink_configuration_type_2 import EventSinkConfigurationType2
  from ..models.event_sink_configuration_type_3 import EventSinkConfigurationType3
  from ..models.event_sink_configuration_type_1 import EventSinkConfigurationType1





T = TypeVar("T", bound="EventSink")


@_attrs_define
class EventSink:
    """ 
        Attributes:
            configuration (Union['EventSinkConfigurationType1', 'EventSinkConfigurationType2',
                'EventSinkConfigurationType3', EventSinkConfigurationType0]): Same as a `EventSinkConfiguration`, but only with
                fields that are safe to share in public, i.e. secrets info removed.
            created_at (datetime.datetime):
            description (str):
            event_sink_type (EventSinkType): The type of event sink. eg. Slack, Jira, etc.
            id (str):
            name (str):
            tenant_id (str):
            updated_at (datetime.datetime):
     """

    configuration: Union['EventSinkConfigurationType1', 'EventSinkConfigurationType2', 'EventSinkConfigurationType3', EventSinkConfigurationType0]
    created_at: datetime.datetime
    description: str
    event_sink_type: EventSinkType
    id: str
    name: str
    tenant_id: str
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.event_sink_configuration_type_2 import EventSinkConfigurationType2
        from ..models.event_sink_configuration_type_3 import EventSinkConfigurationType3
        from ..models.event_sink_configuration_type_1 import EventSinkConfigurationType1
        configuration: Union[Dict[str, Any], str]
        if isinstance(self.configuration, EventSinkConfigurationType0):
            configuration = self.configuration.value
        elif isinstance(self.configuration, EventSinkConfigurationType1):
            configuration = self.configuration.to_dict()
        elif isinstance(self.configuration, EventSinkConfigurationType2):
            configuration = self.configuration.to_dict()
        else:
            configuration = self.configuration.to_dict()


        created_at = self.created_at.isoformat()

        description = self.description

        event_sink_type = self.event_sink_type.value

        id = self.id

        name = self.name

        tenant_id = self.tenant_id

        updated_at = self.updated_at.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "configuration": configuration,
            "created_at": created_at,
            "description": description,
            "event_sink_type": event_sink_type,
            "id": id,
            "name": name,
            "tenant_id": tenant_id,
            "updated_at": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event_sink_configuration_type_2 import EventSinkConfigurationType2
        from ..models.event_sink_configuration_type_3 import EventSinkConfigurationType3
        from ..models.event_sink_configuration_type_1 import EventSinkConfigurationType1
        d = src_dict.copy()
        def _parse_configuration(data: object) -> Union['EventSinkConfigurationType1', 'EventSinkConfigurationType2', 'EventSinkConfigurationType3', EventSinkConfigurationType0]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_event_sink_configuration_type_0 = EventSinkConfigurationType0(data)



                return componentsschemas_event_sink_configuration_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_event_sink_configuration_type_1 = EventSinkConfigurationType1.from_dict(data)



                return componentsschemas_event_sink_configuration_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_event_sink_configuration_type_2 = EventSinkConfigurationType2.from_dict(data)



                return componentsschemas_event_sink_configuration_type_2
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_event_sink_configuration_type_3 = EventSinkConfigurationType3.from_dict(data)



            return componentsschemas_event_sink_configuration_type_3

        configuration = _parse_configuration(d.pop("configuration"))


        created_at = isoparse(d.pop("created_at"))




        description = d.pop("description")

        event_sink_type = EventSinkType(d.pop("event_sink_type"))




        id = d.pop("id")

        name = d.pop("name")

        tenant_id = d.pop("tenant_id")

        updated_at = isoparse(d.pop("updated_at"))




        event_sink = cls(
            configuration=configuration,
            created_at=created_at,
            description=description,
            event_sink_type=event_sink_type,
            id=id,
            name=name,
            tenant_id=tenant_id,
            updated_at=updated_at,
        )

        event_sink.additional_properties = d
        return event_sink

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
