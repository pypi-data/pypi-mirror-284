from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import cast

if TYPE_CHECKING:
  from ..models.list_detection_rules_response_data import ListDetectionRulesResponseData





T = TypeVar("T", bound="CrudApiRequestAndResponseDataForDetectionRuleApiHandlerType1")


@_attrs_define
class CrudApiRequestAndResponseDataForDetectionRuleApiHandlerType1:
    """ 
        Attributes:
            list_resp (ListDetectionRulesResponseData):
     """

    list_resp: 'ListDetectionRulesResponseData'


    def to_dict(self) -> Dict[str, Any]:
        from ..models.list_detection_rules_response_data import ListDetectionRulesResponseData
        list_resp = self.list_resp.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update({
            "ListResp": list_resp,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_detection_rules_response_data import ListDetectionRulesResponseData
        d = src_dict.copy()
        list_resp = ListDetectionRulesResponseData.from_dict(d.pop("ListResp"))




        crud_api_request_and_response_data_for_detection_rule_api_handler_type_1 = cls(
            list_resp=list_resp,
        )

        return crud_api_request_and_response_data_for_detection_rule_api_handler_type_1

