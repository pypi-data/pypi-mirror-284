from typing import Any
from kbrainsdk.validation.messages import validate_create_subscription, validate_servicebus_message, validate_servicebus_queue, validate_servicebus_topic, validate_websocket_group_request
from kbrainsdk.apibase import APIBase

class Messages(APIBase):

    def __init__(self, *args: Any, **kwds: Any) -> Any:
        return super().__init__(*args, **kwds)
    
    def publish_message(self, message: str, topic_name: str, application_properties: dict | None = None) -> None:
        payload = {
            "message": message,
            "topic_name": topic_name,
            "application_properties": application_properties
        }
        
        validate_servicebus_message(payload)
        path = f"/service_bus/send/v1"
        response = self.apiobject.call_endpoint(path, payload, "post")
        return response
    
    def create_topic(self, topic_name: str) -> None:
        payload = {
            "topic_name": topic_name
        }
        
        validate_servicebus_topic(payload)
        path = f"/service_bus/topic/create/v1"
        response = self.apiobject.call_endpoint(path, payload, "post")
        return response

    def create_queue(self, queue_name: str) -> None:
        payload = {
            "queue_name": queue_name
        }
        validate_servicebus_queue(payload)
        path = f"/service_bus/queue/create/v1"
        response = self.apiobject.call_endpoint(path, payload, "post")
        return response

    def create_subscription(self, topic_name: str, subscription_name: str) -> None:
        payload = {
            "topic_name": topic_name,
            "subscription_name": subscription_name
        }
        validate_create_subscription(payload)
        path = f"/service_bus/subscription/create/v1"
        response = self.apiobject.call_endpoint(path, payload, "post")
        return response

    def subscribe_to_websocket_group(self, token: str, group_name: str, client_id: str, tenant_id: str, client_secret: str):
        payload = {
            "token": token,
            "group_name": group_name,
            "client_id": client_id,
            "tenant_id": tenant_id,
            "client_secret": client_secret
        }
        validate_websocket_group_request(payload)
        path = f"/websocket/group/subscribe/v1"
        response = self.apiobject.call_endpoint(path, payload, "post")
        return response

    def authenticate_to_websocket_group(self, token: str, group_name: str, client_id: str, tenant_id: str, client_secret: str):
        payload = {
            "token": token,
            "group_name": group_name,
            "client_id": client_id,
            "tenant_id": tenant_id,
            "client_secret": client_secret
        }
        validate_websocket_group_request(payload)
        path = f"/websocket/group/authenticate/v1"
        response = self.apiobject.call_endpoint(path, payload, "post")
        return response

    def unsubscribe_to_websocket_group(self, token: str, group_name: str, client_id: str, tenant_id: str, client_secret: str):
        payload = {
            "token": token,
            "group_name": group_name,
            "client_id": client_id,
            "tenant_id": tenant_id,
            "client_secret": client_secret
        }
        validate_websocket_group_request(payload)
        path = f"/websocket/group/unsubscribe/v1"
        response = self.apiobject.call_endpoint(path, payload, "post")
        return response

    def get_websocket_group_subscribers(self, token: str, group_name: str, client_id: str, tenant_id: str, client_secret: str):
        payload = {
            "token": token,
            "group_name": group_name,
            "client_id": client_id,
            "tenant_id": tenant_id,
            "client_secret": client_secret
        }
        validate_websocket_group_request(payload)
        path = f"/websocket/group/subscribers/v1"
        response = self.apiobject.call_endpoint(path, payload, "post")
        return response

    

