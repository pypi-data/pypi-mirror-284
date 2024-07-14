import json
import logging
from abc import ABC, abstractmethod

import backoff
from openai import OpenAI, APITimeoutError, APIConnectionError, APIError, InternalServerError, APIResponseValidationError
from pydantic import BaseModel

from rooms_shared_services.src.models.texts.variants import LLMRequestVariant

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

OpenAIServiceError = (APITimeoutError, APIConnectionError, APIError, InternalServerError, APIResponseValidationError)


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

    def run_query(self, temperature: float = 1.0, **request_params) -> str | dict:
        messages = self.collect_messages(request_variant=self.request_variant, **request_params)
        logger.info("Collected messages for llm query")
        for index, message in enumerate(messages):
            logger.info("{}. {}".format(index, message))
        validated_response = self.receive_validated_response(messages=messages, temperature=temperature, **request_params)
        logger.info("LLM validated_response: {}".format(validated_response))
        return validated_response

    @abstractmethod
    def collect_messages(self, **request_params) -> list[OpenaiRequestMessage]:
        ...

    @backoff.on_exception(backoff.constant, json.JSONDecodeError, max_tries=10, interval=1)    
    def receive_validated_response(self, messages: list[OpenaiRequestMessage], temperature: float, **request_params):
        raw_response = self.receive_raw_response(messages=messages, temperature=temperature)
        logger.info("LLM raw response: {}".format(raw_response))
        response_content = raw_response.choices[0].message.content
        logger.info("LLM raw response content: {}".format(response_content))
        return self.validate_json_response(response=response_content, **request_params)
        
    @backoff.on_exception(backoff.constant, OpenAIServiceError, max_tries=10, interval=1)    
    def receive_raw_response(self, messages: list[OpenaiRequestMessage], temperature: float):
        return self.openai_client.chat.completions.create(
            model=self.openai_model,
            messages=[message.model_dump() for message in messages],
            temperature=temperature,
        )

    def validate_json_response(self, response: str, **kwargs) -> str | dict | None:
        logger.info(response)
        validated_response = json.loads(response)["result"]
        logger.info("Deserialized json response: {}".format(validated_response))
        return validated_response
