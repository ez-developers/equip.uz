# (
LANGUAGE = 1
# ) = range(1)


class State:

    def __init__(self, state: int = None):
        self.state = state
        self.states = []

    def set_state(self) -> int:
        return self.state

    def new_state(self, name: str):
        self.states.pop()
