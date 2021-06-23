from population.population import Population
from population.analysis import bucket_ages, pprint_buckets, bucket_genders

population = Population()
population.create_n(1000)
population.ticks(40)

pprint_buckets(bucket_ages(population))
print(bucket_genders(population))