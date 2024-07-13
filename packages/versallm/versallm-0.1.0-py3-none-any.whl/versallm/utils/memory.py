from typing import List


class ConversationalMemory(List):
    def __init__(self) -> None:
        self.chat_history = []

    def __repr__(self) -> str:
        print(self.chat_history)
        return f"ConversationalMemory({self.chat_history})"

    ## to be implemented
    def save_memory(self, location: str = "./"):
        pass
