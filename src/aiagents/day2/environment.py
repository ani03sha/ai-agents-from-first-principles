class Environment:
    def __init__(self, size: int):
        self.size: int = size
        self.state: list[int] = []
        self.goal: tuple[int, int] = (size - 1, size - 1)
        self.blocked_cells: set[tuple[int, int]] = {
            (0, 4),
            (1, 3),
            (2, 1),
            (2, 3),
            (3, 2),
        }

    def reset(self) -> list[int]:
        self.state = [0, 0, self.size, self.size]
        return self.state

    def get_state(self) -> int:
        return self.state

    def apply_action(
        self, action: str
    ) -> tuple[list[int], bool]:
        success_flag: bool = False
        # State changes based on action
        if action == "RIGHT":
            # Move right
            x = min(self.size - 1, self.state[0] + 1)
            y = self.state[1]
            if (x, y) not in self.blocked_cells:
                self.state[0] = x
                success_flag = True
        elif action == "DOWN":
            # Move down
            x = self.state[0]
            y = min(self.size - 1, self.state[1] + 1)
            if (x, y) not in self.blocked_cells:
                self.state[1] = y
                success_flag = True

        state_key = (self.state[0], self.state[1])

        return (self.state, success_flag)

    def is_terminal(self):
        return self.state[0] == self.size - 1 and self.state[1] == self.size - 1
