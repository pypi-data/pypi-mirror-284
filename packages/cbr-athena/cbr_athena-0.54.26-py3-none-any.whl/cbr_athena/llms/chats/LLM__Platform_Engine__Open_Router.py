from urllib.parse import urljoin

import requests

from cbr_athena.llms.chats.LLM__Platform_Engine import LLM__Platform_Engine
from cbr_athena.llms.providers.open_router.LLM__Open_Router import LLM__Open_Router
from cbr_athena.schemas.for_fastapi.LLMs__Chat_Completion import LLMs__Chat_Completion
from osbot_utils.testing.Logging import Logging
from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Json import from_json_str


class LLM__Platform_Engine__Open_Router(LLM__Platform_Engine):
    llm_platform       : str
    llm_provider       : str
    llm_model          : str
    llm_chat_completion: LLMs__Chat_Completion
    llm_open_router    : LLM__Open_Router

    def execute_request(self):
        # user_prompt = self.llm_chat_completion.user_prompt          # todo add history and other types of messages
        # self.llm_open_router.add_message__user(user_prompt)
        # return self.llm_open_router.chat_completion__streamed()
        with self.llm_open_router as _:
            _.add_messages__system(self.llm_chat_completion.system_prompts)
            _.add_histories       (self.llm_chat_completion.histories)
            _.add_message__user   (self.llm_chat_completion.user_prompt )
            _.set_model           (self.llm_model)
            return _.chat_completion__streamed()



