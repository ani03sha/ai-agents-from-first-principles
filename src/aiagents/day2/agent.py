from aiagents.day2.environment import Environment
from aiagents.day2.policy import Policy


class Agent:
    def __init__(self, policy: Policy, environment: Environment):
        self.policy = policy
        self.environment = environment
        self.memory: dict[tuple[int, int], set[str]] = {}

    def act(self, state: list[int]) -> None:
        while not self.environment.is_terminal():
            state_key = (state[0], state[1])
            
            actions = self.policy.get_actions(state)
            
            # Failed actions
            failed_actions = self.memory.get(state_key, set())
            
            available_actions = [action for action in actions if action not in failed_actions]
            
            if not available_actions:
                return
            
            action = available_actions[0]
            
            # Apply the action
            state, success = self.environment.apply_action(action)

            # If the last action resulted in blocked cell,
            # we store it in the memory so that we don't 
            # repeat it
            if not success:
                self.memory.setdefault(state_key, set()).add(action)
                
            print(f"State becomes {state}")
        print("Reached at the bottom right corner of the grid")
