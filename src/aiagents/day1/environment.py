class Environment:
    def __init__(self, size: int):
        self.size: int = size
        self.state: list[int] = []
        self.goal: tuple[int, int] = (size - 1, size - 1)

    def reset(self) -> list[int]:
        self.state = [0, 0, self.size, self.size]
        return self.state

    def get_state(self) -> int:
        return self.state

    def apply_action(self, action: str) -> list[int]:
        # State changes based on action
        if action == "RIGHT":
            # Move right
            self.state[0] = min(self.size - 1, self.state[0] + 1)
        elif action == "DOWN":
            # Move down
            self.state[1] = min(self.size - 1, self.state[1] + 1)

        return self.state

    def is_terminal(self):
        return self.state[0] == self.size - 1 and self.state[1] == self.size - 1
