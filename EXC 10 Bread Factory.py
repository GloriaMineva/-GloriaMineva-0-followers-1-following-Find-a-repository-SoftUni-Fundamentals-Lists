total_energy = 100
coins = 100
events = list(input().split('|'))
events = list(element.split('-') for element in events)
for index in range(len(events)):
    if events[index][0] == 'rest':
        initial_energy = total_energy
        total_energy += int(events[index][1])
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - initial_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {total_energy}.')
    elif events[index][0] == 'order':
        if total_energy >= 30:
            total_energy -= 30
            coins += int(events[index][1])
            print(f'You earned {int(events[index][1])} coins.')
        else:
            total_energy += 50
            print('You had to rest!')

    else:
        if coins > int(events[index][1]):
            coins -= int(events[index][1])
            print(f'You bought {events[index][0]}.')
        else:
            print(f'Closed! Cannot afford {events[index][0]}.')
            exit()
print('Day completed!')
print(f'Coins: {coins}')
print(f'Energy: {total_energy}')






