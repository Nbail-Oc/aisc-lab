import random
# Fitness function
def fitness(x):
    return x * x
# Initial population
population = [random.randint(0, 31) for _ in range(10)]
# Genetic Algorithm
for generation in range(20):
    # Sort population by fitness
    population.sort(key=fitness, reverse=True)
    # Select best 5 parents
    parents = population[:5]
    # Elitism: keep best 2
    new_population = parents[:2]
    # Generate children
    while len(new_population) < 10:
        # Select two parents
        p1 = random.choice(parents)
        p2 = random.choice(parents)
        # Crossover
        child = (p1 + p2) // 2
        # Mutation
        if random.random() < 0.1:
            child += random.choice([-1, 1])
        # Keep value in range 0 to 31
        child = max(0, min(31, child))
        new_population.append(child)
    population = new_population
# Find best solution
best = max(population, key=fitness)
print("Best Solution:", best)
print("Best Fitness:", fitness(best))
