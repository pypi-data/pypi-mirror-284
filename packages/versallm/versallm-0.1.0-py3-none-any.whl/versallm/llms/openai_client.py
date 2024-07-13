from .base import VersaLLM


class OpenAIClient(VersaLLM):

    def __init__(
        self,
        model: str = None,
        api_key: str = None,
        temperature: int = 0,
        max_output_token: int = 1024,
        **kwargs
    ) -> None:
        super().__init__(model, api_key, temperature, max_output_token, **kwargs)

    def __repr__(self) -> str:
        return "Open AI Client"
