from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="MessageSubscriberAuthTokenOut")


@attr.s(auto_attribs=True)
class MessageSubscriberAuthTokenOut:
    """
    Attributes:
        bridge_config (str):
        token (str):
    """

    bridge_config: str
    token: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bridge_config = self.bridge_config
        token = self.token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bridgeConfig": bridge_config,
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bridge_config = d.pop("bridgeConfig")

        token = d.pop("token")

        message_subscriber_auth_token_out = cls(
            bridge_config=bridge_config,
            token=token,
        )

        message_subscriber_auth_token_out.additional_properties = d
        return message_subscriber_auth_token_out

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
