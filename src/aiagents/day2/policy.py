class Policy:
    def __init__(self):
        pass

    def get_actions(self, state: list[int]) -> list[str]:
        x, y, max_x, max_y = state
        actions: list[str] = []
        if x < max_x - 1:
            actions.append("RIGHT")
        if y < max_y - 1:
            actions.append("DOWN")    

        return actions
