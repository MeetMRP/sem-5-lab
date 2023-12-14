import numpy


def initialize_population(population_size, lb, ub):
    return numpy.random.uniform(lb, ub, population_size)


def calculate_fitness(population):
    return numpy.sum(population * population, axis=1)


def select_parents(population, fitness, mating_pool_size):
    parents = numpy.empty((mating_pool_size, population.shape[1]))
    for p in range(mating_pool_size):
        fittest_index = numpy.argmax(fitness)
        parents[p, :] = population[fittest_index, :]
        fitness[fittest_index] = -1
    return parents


def crossover(parents, offspring_size, genes):
    offspring = numpy.empty((offspring_size, parents.shape[1]))
    for k in range(offspring_size):
        crossover_point = numpy.random.randint(0, genes)
        parent1_index = k % parents.shape[0]
        parent2_index = (k + 1) % parents.shape[0]
        offspring[k, :crossover_point] = parents[parent1_index, :crossover_point]
        offspring[k, crossover_point:] = parents[parent2_index, crossover_point:]
    return offspring


def mutate(offspring, lb, ub):
    for index in range(offspring.shape[0]):
        random_index = numpy.random.randint(0, offspring.shape[1])
        random_value = numpy.random.uniform(lb, ub, 1)
        offspring[index, random_index] += random_value
    return offspring


def create_new_generation(population, parents, offspring):
    population[:parents.shape[0], :] = parents
    population[parents.shape[0]:, :] = offspring
    return population


def find_fittest_individual(population, fitness):
    fittest_index = numpy.argmax(fitness)
    return population[fittest_index, :], fitness[fittest_index]


# Parameters
genes = 2
chromosomes = 10
mating_pool_size = 6
offspring_size = chromosomes - mating_pool_size
lb, ub = -5, 5
population_size = (chromosomes, genes)
generations = 3

# Algorithm
population = initialize_population(population_size, lb, ub)

for generation in range(generations):
    print(f"Generation: {generation + 1}")
    fitness = calculate_fitness(population)
    parents = select_parents(population, fitness.copy(), mating_pool_size)
    offspring = crossover(parents, offspring_size, genes)
    offspring = mutate(offspring, lb, ub)
    population = create_new_generation(population, parents, offspring)
    best_ind, best_fitness = find_fittest_individual(population, fitness)
    print("New Population for next generation:")
    print(population)
    print("Best Individual:")
    print(best_ind)
    print("Best Individual's Fitness:")
    print(best_fitness)
    print()
