from population.population import Population

agents = Population()
agents.create_n(10)
agents.age_agents()
agents.age_agents()

for a in agents.agents:
    print(a)
print(agents.bucket_ages())