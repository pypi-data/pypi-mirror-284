from cbr_athena.schemas.for_fastapi.LLMs__Chat_Completion import LLMs__Chat_Completion
from osbot_utils.base_classes.Type_Safe import Type_Safe

from osbot_utils.helpers.Local_Caches import Local_Caches
from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Files import path_combine, folder_create
from osbot_utils.utils.Json import from_json_str
from osbot_utils.utils.Misc import is_guid, random_guid, date_time_now

CACHE_NAME__CHATS_CACHE =  'chats_cache'


class CBR__Chats_Storage__Local(Type_Safe):
    chats_cache : Local_Caches

    def __init__(self):
        super().__init__()
        self.chats_cache.caches_name =  CACHE_NAME__CHATS_CACHE

    def save_chat(self, llm_chat_completion: LLMs__Chat_Completion):
        chat_id = llm_chat_completion.chat_thread_id

        if chat_id is None or is_guid(chat_id) is False:
            chat_id = llm_chat_completion.chat_thread_id = random_guid()
        chat_cache = self.chats_cache.cache(chat_id)
        cache_key  = date_time_now()
        cache_data = from_json_str(llm_chat_completion.json())
        chat_cache.add(cache_key, cache_data)
        chat_cache.add('latest', cache_data)
        pprint(f"Save chat with id: {chat_id}")
        return cache_key

    def chat_cache(self, chat_id):
        return self.chats_cache.cache(chat_id)

    def cached_ids(self):
        return self.chats_cache.existing_cache_names()

    def setup(self):
        self.chats_cache.setup()                                    # make sure the caches folder existgs
        return self