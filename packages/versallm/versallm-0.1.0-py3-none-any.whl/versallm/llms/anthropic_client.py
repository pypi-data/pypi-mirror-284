import anthropic
from .base import VersaLLM
from ..utils.memory import ConversationalMemory


class AnthropicClient(VersaLLM):
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
        return "Anthropic Client"

    def completion(self, user_prompt, system_prompt, tools=[]):
        client = anthropic.Anthropic()

        user_message = {"role": "user", "content": user_prompt}

        self.memory.chat_history.append(user_message)

        response = client.messages.create(
            model=self.model,
            system=system_prompt,
            temperature=self.temperature,
            max_tokens=self.max_output_tokens,
            messages=self.memory.chat_history,
            tools=tools,
        )

        assistant_message = {"role": "assistant", "content": response.content[0].text}

        self.memory.chat_history.append(assistant_message)

        return response