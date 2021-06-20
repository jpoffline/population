from typing import List
from population.agent import Agent


class Population:
    def __init__(self) -> None:
        self.agents: List[Agent] = []

    @property
    def currid(self):
        return len(self.agents)

    def add_new(self):
        self.agents.append(Agent.new(self.currid))

    def birth_from(self, parent):
        self.agents.append(parent.give_birth(self.currid))

    def create_n(self, n):
        [self.add_new() for _ in range(n)]

    def age_agents(self, amount=1):
        [agent.make_older(amount) for agent in self.agents]
        self.reproduce_agents()

    def reproduce_agents(self):
        for agent in self.agents:
            if agent.reproduce:
                self.birth_from(agent)

    def bucket_ages(self):
        ages = {}
        for agent in self.agents:
            if not agent.alive:
                continue
            age = agent.age
            if age not in ages:
                ages[age] = 0
            ages[age] += 1
        return ages
