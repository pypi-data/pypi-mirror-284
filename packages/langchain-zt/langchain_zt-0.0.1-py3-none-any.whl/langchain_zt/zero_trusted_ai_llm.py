import json
from typing import Optional, List, Any

import requests
from langchain_core.callbacks import CallbackManagerForLLMRun
from langchain_core.language_models import LanguageModelInput
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import BaseMessage
from langchain_core.outputs import ChatResult
from langchain_core.runnables import RunnableConfig


class ZeroTrustedAI(BaseChatModel):
    def __int__(self, bearer_token: str, environment: str) -> None:
        self.bearer_token = bearer_token
        self.environment = environment

        if self.environment == "staging":
            self.environment_app_url = "https://staging-app.zerotrusted.ai"
            self.environment_api_url = (
                "https://zt-ml-llm-staging.azurewebsites.net/zt-llm-report-V2"
            )

    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> ChatResult:
        # Implementation here
        pass

    def _llm_type(self):
        # Implementation here
        pass

    def invoke(
        self,
        input: LanguageModelInput,
        LLM,
        config: Optional[RunnableConfig] = None,
        *,
        stop: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> BaseMessage:
        payload = json.dumps({"Prompt": input, "LLMs": LLM})
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.9",
            "Authorization": self.bearer_token,
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Origin": self.environment_app_url,
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
        }

        response = requests.request(
            "POST", self.environment_api_url, headers=headers, data=payload
        )

        # print(response.text)
        return response.text
