from typing import List, Dict

from llama_index.core.llms import ChatMessage, CustomLLM
from llama_index.storage.chat_store.redis import RedisChatStore

from chatbot.utils.translator import Translator


class CacheChatStore:
    """A class to store chat messages in a cache."""

    def __init__(
        self,
        host: str,
        port: int,
        db: int,
        username: str,
        password: str,
        llm: CustomLLM,
        live_time_seconds: int = 86400,
        max_messages_pairs: int = 5,
    ):
        self.chat_client = RedisChatStore(
            redis_url=f"redis://{username}:{password}@{host}:{port}/{db}",
            ttl=live_time_seconds,
        )
        self.max_messages_pairs = (
            max_messages_pairs + 1
            if max_messages_pairs % 2 != 0
            else max_messages_pairs
        )  # Ensure even number of messages
        self.en_translator = Translator(
            source="auto", target="english", capitalize_sentences=True
        )
        self.llm = llm

    def chat_messages_to_dict(self, messages: List[str], en_translate=False) -> List[Dict[str, str]]:
        """Convert chat messages to LLM chat format with translation."""

        messages_dict = []
        for message in messages:
            content = (
                message.content
                if not en_translate
                else self.en_translator.translate(message.content)
            )
            messages_dict.append({"role": message.role.value, "content": content})
        return messages_dict

    def trim_messages(self, key: str) -> List[ChatMessage]:
        """Trim the messages if the number of messages exceeds the limit."""

        # We store messages in pairs of user and assistant messages
        max_messages = self.max_messages_pairs * 2

        # Get all messages
        messages = self.chat_client.get_messages(key)

        keep_messages = messages[-max_messages:]
        self.chat_client.set_messages(key, keep_messages)
        remove_messages = messages[:-max_messages]

        return remove_messages

    async def async_trim_messages(self, key: str) -> List[ChatMessage]:
        """Trim the messages if the number of messages exceeds the limit asynchronously."""

        # We store messages in pairs of user and assistant messages
        max_messages = self.max_messages_pairs * 2

        # Get all messages
        messages = await self.chat_client.aget_messages(key)

        keep_messages = messages[-max_messages:]
        await self.chat_client.aset_messages(key, keep_messages)
        remove_messages = messages[:-max_messages]

        return remove_messages
    
    def add_system_message(self, key: str, message: str) -> List[Dict[str, str]]:
        """Add a system message to the chat store."""

        # Add the system message
        system_message = ChatMessage(role="system", content=message)
        self.chat_client.add_message(key, system_message)

        # Trim the messages if the number of messages exceeds the limit
        removed_messages = self.trim_messages(key)
        if removed_messages:
            return self.chat_messages_to_dict(removed_messages)

        return None
    
    async def async_add_system_message(self, key: str, message: str) -> List[Dict[str, str]]:
        """Add a system message to the chat store asynchronously."""

        # Add the system message
        system_message = ChatMessage(role="system", content=message)
        await self.chat_client.async_add_message(key, system_message)

        # Trim the messages if the number of messages exceeds the limit
        removed_messages = await self.async_trim_messages(key)
        if removed_messages:
            return self.chat_messages_to_dict(removed_messages)

        return None

    def add_message_pair(self, key: str, query: str, response: str) -> List[Dict[str, str]]:
        """Add a query-response message pair to the chat store."""

        message_pair = [
            ChatMessage(role="user", content=query),
            ChatMessage(role="assistant", content=response),
        ]
        for message in message_pair:
            self.chat_client.add_message(key, message)

        # Trim the messages if the number of messages exceeds the limit
        removed_messages = self.trim_messages(key)
        if removed_messages:
            return self.chat_messages_to_dict(removed_messages)

        return None

    async def async_add_message_pair(self, key: str, query: str, response: str) -> List[Dict[str, str]]:
        """Add a query-response message pair to the chat store asynchronously."""

        message_pair = [
            ChatMessage(role="user", content=query),
            ChatMessage(role="assistant", content=response),
        ]
        for message in message_pair:
            await self.chat_client.async_add_message(key, message)

        # Trim the messages if the number of messages exceeds the limit
        removed_messages = await self.async_trim_messages(key)
        if removed_messages:
            return self.chat_messages_to_dict(removed_messages)

        return None

    def get_chat_history(self, key: str, en_translate=False) -> List[Dict[str, str]]:
        """Get the chat history from the chat store."""
        messages = self.chat_client.get_messages(key)
        return self.chat_messages_to_dict(messages, en_translate)

    async def async_get_chat_history(
        self, key: str, en_translate=False
    ) -> List[Dict[str, str]]:
        """Get the chat history from the chat store asynchronously."""
        messages = await self.chat_client.aget_messages(key)
        return self.chat_messages_to_dict(messages, en_translate)

    def clear_messages(self, key: str):
        """Clear the messages of the user from the chat store."""
        self.chat_client.delete_messages(key)
        return None

    async def async_clear_messages(self, key: str) -> None:
        """Clear the messages of the user from the chat store asynchronously."""
        await self.chat_client.adelete_messages(key)
        return None
