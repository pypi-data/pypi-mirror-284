import typing
import os
import uuid
import datetime as dt
from importlib.metadata import version
from concurrent.futures import ThreadPoolExecutor

from .api_client.client import (
    NeuralTrustApi,
    TraceResponse,
    TraceTask
)

OMIT = typing.cast(typing.Any, ...)

DEFAULT_BASE_URL = "https://api.neuraltrust.ai/v1"

def add_sdk_info(tags):
    tags["$sdk"] = "python"
    tags["$sdk.version"] = version("neuraltrust")
    return tags

class NeuralTrust:
    base_client: NeuralTrustApi
    executor: ThreadPoolExecutor

    def __init__(
        self,
        api_key: typing.Union[str, None] = None,
        base_url: typing.Union[str, None] = None,
        timeout: typing.Union[float, None] = None,
        max_workers: typing.Union[int, None] = None,
    ) -> None:
        
        if not api_key:
            api_key = os.environ.get("NEURALTRUST_API_KEY")
        
        self.trace_executor = ThreadPoolExecutor(max_workers=max_workers)
        self.base_client = NeuralTrustApi(
            api_key=api_key, base_url=DEFAULT_BASE_URL, timeout=timeout
        )
        # set base URL
        if os.environ.get("NEURALTRUST_BASE_URL"):
            self.base_client._client_wrapper._base_url = os.environ["NEURALTRUST_BASE_URL"]
        if base_url:
            self.base_client._client_wrapper._base_url = base_url

    @property
    def api_key(self) -> typing.Union[str, None]:
        """Property getter for api_key."""
        return self.base_client._client_wrapper.api_key

    @api_key.setter
    def api_key(self, value: typing.Union[str, None]) -> None:
        """Property setter for api_key."""
        self.api_key = value
        if value is not None:
            self.base_client._client_wrapper.api_key = value

    @property
    def base_url(self) -> typing.Union[str, None]:
        """Property getter for base_url."""
        return self.base_client._client_wrapper._base_url

    @base_url.setter
    def base_url(self, value: typing.Union[str, None]) -> None:
        """Property setter for base_url."""
        if value is not None:
            self.base_client._client_wrapper._base_url = value

    def init_conversation(self, conversation_id: str = None) -> "Conversation":
        return Conversation(client=self, conversation_id=conversation_id)
    
    def trace(
        self,
        *,
        id: typing.Optional[int] = OMIT,
        task: typing.Optional[TraceTask] = OMIT,
        input: typing.Optional[str] = OMIT,
        output: typing.Optional[str] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        conversation_id: typing.Optional[str] = OMIT,
        interaction_id: typing.Optional[str] = OMIT,
        message_id: typing.Optional[str] = OMIT,
        timestamp: typing.Optional[dt.datetime] = OMIT
    ) -> TraceResponse:
        return self.base_client.trace(
            id=id,
            task=task,
            input=input,
            output=output,
            user_id=user_id,
            conversation_id=conversation_id,
            interaction_id=interaction_id,
            message_id=message_id,
            timestamp=timestamp
        )

    def trace_async(
        self,
        *,
        id: typing.Optional[int] = OMIT,
        task: typing.Optional[TraceTask] = OMIT,
        input: typing.Optional[str] = OMIT,
        output: typing.Optional[str] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        conversation_id: typing.Optional[str] = OMIT,
        interaction_id: typing.Optional[str] = OMIT,
        message_id: typing.Optional[str] = OMIT,
        timestamp: typing.Optional[dt.datetime] = OMIT
    ):
        return self.trace_executor.submit(
            self.trace,
            id=id,
            task=task,
            input=input,
            output=output,
            user_id=user_id,
            conversation_id=conversation_id,
            interaction_id=interaction_id,
            message_id=message_id,
            timestamp=timestamp
        )

class Message:
    def __init__(self, client, conversation_id: str, message_id: str = None):
        self.client = client
        self.message_id = message_id or str(uuid.uuid4())
        self.interaction_id = str(uuid.uuid4())
        self.conversation_id = conversation_id
        self.timestamp = dt.datetime.now()

    def send_retrieval(self, input: str, output: str):
        self.input = input
        self.output = output
        self._send_trace("retrieval")

    def send_generation(self, input: str, output: str):
        self.input = input
        self.output = output
        self._send_trace("generation")

    def send_router(self, input: str, output: str):
        self.input = input
        self.output = output
        self._send_trace("router")

    def _send_trace(self, task: str):
        self.client.trace_async(
            conversation_id=self.conversation_id,
            interaction_id=self.interaction_id,
            message_id=self.message_id,
            input=self.input,
            output=self.output,
            task=task,
            timestamp=self.timestamp
        )

class Conversation:
    def __init__(self, client: NeuralTrust, conversation_id: str = None):
        self.conversation_id = conversation_id or str(uuid.uuid4())
        self.client = client

    def init_message(self, message_id: str = None) -> Message:
        message = Message(client=self.client, conversation_id=self.conversation_id, message_id=message_id)
        return message