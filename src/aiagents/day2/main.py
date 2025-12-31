from aiagents.day2.agent import Agent
from aiagents.day2.environment import Environment
from aiagents.day2.policy import Policy


def main():
    environment = Environment(size=5)
    policy = Policy()
    agent = Agent(policy, environment)

    state = environment.reset()

    print(f"Start state: {state}")

    agent.act(state)


if __name__ == "__main__":
    main()
