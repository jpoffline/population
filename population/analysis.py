from population.population import Population


def bucket_ages(population: Population):
    ages = {}
    for agent in population:
        if not agent.alive:
            continue
        age = agent.age.age
        if age not in ages:
            ages[age] = 0
        ages[age] += 1
    return ages


def bucket_genders(population: Population):
    genders = {}
    for agent in population:
        if not agent.alive:
            continue
        gender = agent.gender.gender
        if not gender in genders:
            genders[gender] = 0
        genders[gender] += 1
    return genders


def pprint_buckets(buckets):
    ages = list(buckets.keys())
    population_size = sum(buckets.values())
    ages.sort(reverse=True)
    sorted = []
    for age in ages:
        sorted.append(
            (age, buckets[age], round(buckets[age] / population_size * 100, 3))
        )
    print(sorted)