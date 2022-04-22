from numpy.random import rand, randint
import numpy as np
import matplotlib.pyplot as plt

def objective_functions(I):
    x = I[0]
    y = I[1]
    Objective_min = 0.26*(x**2 + y**2) - 0.48*x*y
    Objective_max = 1/(1 + Objective_min)

    return Objective_max

bounds = [[-10, 10], [-10, 10]]
iteration = 200
bits = 20
pop_size = 50
crossover_rate = 0.7
mutation_rate = 0.3

def crossover(pop, crossover_rate):
    offspring = list()
    for i in range(int(len(pop)/2)):
        p1 = pop[2*i-1].copy()
        p2 = pop[2*i].copy()
        if rand() < crossover_rate:
            cp = randint(1, len(p1)-1, size=2)
            while cp[0] == cp[1]:
                cp = randint(1, len(p1)-1, size=2)

            cp = sorted(cp)
            c1 = p1[:cp[0]] + p2[cp[0]:cp[1]] + p1[cp[1]:]
            c2 = p2[:cp[0]] + p1[cp[0]:cp[1]] + p2[cp[1]:]
            offspring.append(c1)
            offspring.append(c2)
        else:
            offspring.append(p1)
            offspring.append(p2)

    return offspring

def mutation(pop, mutation_style):
    offspring = list()
    for i in range(int(len(pop))):
        p1 = pop[i].copy()
        if rand() < mutation_rate:
            cp = randint(0, len(p1))
            c1 = p1
            if c1[cp] == 1:
                c1[cp] = 0
            else:
                c1[cp] = 1

            offspring.append(c1)
        else:
            offspring.append(p1)

    return offspring

def selection(pop, fitness, pop_size):
    next_generation = list()
    elite = np.argmax(fitness)
    next_generation.append(pop[elite])
    P = [f/sum(fitness) for f in fitness]
    index = list(range(int(len(pop))))
    index_selected = np.random.choice(index, size=pop_size-1, replace=False, p=P)
    s = 0
    for j in range(pop_size-1):
        next_generation.append(pop[index_selected[s]])
        s += 1

    return next_generation

def generation(bounds, bits, chromosome):
    real_chromosome = list()
    for i in range(len(bounds)):
        st, en = i * bits, (i * bits)+bits
        sub = chromosome[st:en]
        chars = ''.join([str(s) for s in sub])
        integer = int(chars, 2)
        real_value = bounds[i][0] + (integer/(2**bits)) * (bounds[i][1] - bounds[i][0])
        real_chromosome.append(real_value)

    return real_chromosome

pop = [randint(0, 2, bits*len(bounds)).tolist() for _ in range(pop_size)]

best_fitness = []
for gen in range(iteration):
    offspring = crossover(pop, crossover_rate)
    offspring = mutation(offspring, mutation_rate)

    for s in offspring:
        pop.append(s)

    real_chromosome = [generation(bounds, bits, p) for p in pop]
    fitness = [objective_functions(d) for d in real_chromosome]

    index = np.argmax(fitness)
    current_best = pop[index]
    best_fitness.append(1/max(fitness) - 1)
    pop = selection(pop, fitness, pop_size)

fig = plt.figure()
plt.plot(best_fitness)
fig.suptitle('Evolution of the best chromosome')
plt.xlabel('Iteration')
plt.ylabel('Objective function value')
print('Min objective function value: ',min(best_fitness))
print("Optimal solution", generation(bounds, bits, current_best))