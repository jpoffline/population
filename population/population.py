from random import random
from typing import List
from agent.agent import Agent


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

    def ticks(self, times):
        for _ in range(times):
            self.tick()

    def tick(self):
        self.age_agents()
        self.reproduce_agents()

    def age_agents(self, amount=1):
        [agent.make_older(amount) for agent in self.agents if agent.alive]

    def reproduce_agents(self):
        for agent in self.agents:
            if agent.will_reproduce:
                self.birth_from(agent)

    def __iter__(self):
        for agent in self.agents:
            yield agent

    def jsonify(self):
        return [agent.jsonify() for agent in self]