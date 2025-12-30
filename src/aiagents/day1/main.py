from aiagents.day1.agent import Agent
from aiagents.day1.environment import Environment
from aiagents.day1.policy import Policy


def main():
    environment = Environment(size=3)
    policy = Policy()
    agent = Agent(policy, environment)

    state = environment.reset()

    print(f"Start state: {state}")

    agent.act(state)


if __name__ == "__main__":
    main()
