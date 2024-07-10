from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import cast

if TYPE_CHECKING:
  from ..models.delete_detection_rule_response_data import DeleteDetectionRuleResponseData





T = TypeVar("T", bound="CrudApiRequestAndResponseDataForDetectionRuleApiHandlerType7")


@_attrs_define
class CrudApiRequestAndResponseDataForDetectionRuleApiHandlerType7:
    """ 
        Attributes:
            delete_resp (DeleteDetectionRuleResponseData):
     """

    delete_resp: 'DeleteDetectionRuleResponseData'


    def to_dict(self) -> Dict[str, Any]:
        from ..models.delete_detection_rule_response_data import DeleteDetectionRuleResponseData
        delete_resp = self.delete_resp.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update({
            "DeleteResp": delete_resp,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.delete_detection_rule_response_data import DeleteDetectionRuleResponseData
        d = src_dict.copy()
        delete_resp = DeleteDetectionRuleResponseData.from_dict(d.pop("DeleteResp"))




        crud_api_request_and_response_data_for_detection_rule_api_handler_type_7 = cls(
            delete_resp=delete_resp,
        )

        return crud_api_request_and_response_data_for_detection_rule_api_handler_type_7

