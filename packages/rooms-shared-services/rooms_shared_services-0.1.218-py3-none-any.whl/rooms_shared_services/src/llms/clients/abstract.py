import json
import logging
from abc import ABC, abstractmethod

import backoff
from openai import OpenAI
from pydantic import BaseModel

from rooms_shared_services.src.models.texts.variants import LLMRequestVariant

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class OpenaiRequestMessage(BaseModel):
    role: str
    content: str  # noqa: WPS110


class AbstractLLMJSONQueryClient(ABC):
    ...


class AbstractOpenaiJSONQueryClient(AbstractLLMJSONQueryClient):
    def __init__(
        self,
        request_variant: LLMRequestVariant,
        openai_model: str = "gpt-3.5-turbo",
        retry_count: int = 25,
    ):
        """Set attributes.

        Args:
            openai_model (str): __description__.
            request_variant (LLMRequestVariant): _description_.
            retry_count (int): _description_. Defaults to 25
        """
        self.openai_model = openai_model
        self.request_variant = request_variant
        self.openai_client = OpenAI()
        self.retry_count = retry_count

    @backoff.on_exception(backoff.constant, Exception, max_tries=5, interval=1)
    def run_query(self, **request_params) -> str | dict:
        for _ in range(self.retry_count):
            messages = self.collect_messages(request_variant=self.request_variant, **request_params)
            logger.info("Collected messages for llm query")
            for index, message in enumerate(messages):
                logger.info("{}. {}".format(index, message))
            response = self.receive_response(messages=messages)
            response = response.choices[0].message.content
            logger.info("LLM response content: {}".format(response))
            validated_response = self.validate_json_response(response=response, **request_params)
            logger.info("Validated by base validation llm response: {}".format(validated_response))
            return validated_response

    @abstractmethod
    def collect_messages(self, **request_params) -> list[OpenaiRequestMessage]:
        ...

    def receive_response(self, messages: list[OpenaiRequestMessage]):
        return self.openai_client.chat.completions.create(
            model=self.openai_model,
            messages=[message.model_dump() for message in messages],
        )

    def validate_json_response(self, response: str, **kwargs) -> str | dict | None:
        logger.info(response)
        return json.loads(response)["result"]
