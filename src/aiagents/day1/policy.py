class Policy:
    def __init__(self):
        pass

    def select_action(self, state: list[int]) -> str:
        x, y, max_x, max_y = state
        if x < max_x - 1:
            return "RIGHT"
        elif y < max_y - 1:
            return "DOWN"

        raise RuntimeError("No valid actions available")
