from population.population import Population
from population.analysis import bucket_ages, pprint_buckets, bucket_genders

population = Population()
population.create_n(10)
population.ticks(4)

pprint_buckets(bucket_ages(population))
print(bucket_genders(population))
print(population.jsonify())