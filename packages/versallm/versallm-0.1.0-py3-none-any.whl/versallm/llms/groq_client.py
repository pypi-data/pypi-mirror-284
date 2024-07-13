from groq import Groq
from .base import VersaLLM
from ..utils.memory import ConversationalMemory


class GroqClient(VersaLLM):
    def __init__(
        self,
        model: str = None,
        api_key: str = None,
        temperature: int = 0,
        max_output_tokens: int = 1024,
        memory: ConversationalMemory = ConversationalMemory(),
        **kwargs
    ) -> None:
        super().__init__(
            model, api_key, temperature, max_output_tokens, memory, **kwargs
        )

    def __repr__(self) -> str:
        return "Grok Client"

    def completion(self, user_prompt, tools=None, system_prompt=""):
        client = Groq()

        if len(self.memory.chat_history) == 0:
            system_message = {"role": "system", "content": system_prompt}
            self.memory.chat_history.append(system_message)

        user_message = {"role": "user", "content": user_prompt}
        self.memory.chat_history.append(user_message)
        # print(self.memory.chat_history)

        response = client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            max_tokens=self.max_output_tokens,
            messages=self.memory.chat_history,
            tools=tools,
        )
        return response
