from aiagents.day1.environment import Environment
from aiagents.day1.policy import Policy


class Agent:
    def __init__(self, policy: Policy, environment: Environment):
        self.policy = policy
        self.environment = environment

    def act(self, state: list[int | list[str]]) -> None:
        while not self.environment.is_terminal():
            action = self.policy.select_action(state)
            print(f"Action taken: {action}")
            state = self.environment.apply_action(action)
            print(f"State becomes {state}")
        print("Reached at the bottom right corner of the grid")
