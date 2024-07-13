from openai import OpenAI


from ..utils.memory import ConversationalMemory


class VersaLLM:
    def __new__(cls, model: str = None):
        if cls is VersaLLM:
            from .groq_client import GroqClient
            from .openai_client import OpenAIClient
            from .anthropic_client import AnthropicClient

            groq_models = [
                "llama3-8b-8192",
                "llama3-70b-8192",
                "mixtral-8x7b-32768",
                "gemma-7b-it",
                "gemma2-9b-it",
                "whisper-large-v3",
            ]
            openai_models = [
                "gpt-4o",
                "gpt-4-turbo",
                "gpt-4",
                "gpt-3.5-turbo",
                "gpt-3.5-turbo-1106",
                "gpt-3.5-turbo-instruct",
            ]
            anthropic_models = [
                "claude-3-opus-20240229",
                "claude-3-sonnet-20240229",
                "claude-3-haiku-20240307",
            ]

            if model in groq_models:
                return super().__new__(GroqClient)

            elif model in openai_models:
                return super().__new__(OpenAIClient)

            elif model in anthropic_models:
                return super().__new__(AnthropicClient)

            else:
                raise ValueError(f"{model} not found!")

    def __init__(
        self,
        model: str = None,
        api_key: str = None,
        temperature: int = 0,
        max_output_tokens: int = 1024,
        memory: ConversationalMemory = ConversationalMemory(),
        **kwargs,
    ) -> None:
        self.model = model
        self.api_key = api_key
        self.temperature = temperature
        self.max_output_tokens = max_output_tokens
        self.memory = memory
        self.kwargs = kwargs

    def completion(self, system_prompt, user_prompt, tools=None):
        client = OpenAI()

        if len(self.memory) == 0:
            system_message = {"role": "system", "content": system_prompt}
            self.memory.append(system_message)

        user_message = {"role": "user", "content": user_prompt}
        self.memory.append(user_message)

        response = client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            max_tokens=self.max_output_tokens,
            messages=self.memory,
            tools=tools,
        )

        return response
