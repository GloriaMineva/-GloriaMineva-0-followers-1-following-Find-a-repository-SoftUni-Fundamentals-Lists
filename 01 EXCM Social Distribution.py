population = list(map(int, input().split(', ')))
lowest_wealth = int(input())
wealthiest = max(population)
for index in range(len(population)):
    wealthiest_index = population.index(max(population))
    if population[index] < lowest_wealth:
        difference = lowest_wealth - population[index]
        if population[wealthiest_index] - difference >= lowest_wealth:
            population[index] += difference
            population[wealthiest_index] -= difference
        else:
            print('No equal distribution possible')
            exit()
print(population)