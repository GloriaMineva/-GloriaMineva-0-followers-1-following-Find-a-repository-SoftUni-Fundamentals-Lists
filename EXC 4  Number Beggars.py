sums_string = input()
count_of_beggars = int(input())
money_list = [int(x) for x in sums_string.split(', ')]
beggars_list = []
starting_index = 0
for current_beggar in range(count_of_beggars):
    current_sum = 0
    for index in range(starting_index, len(money_list), count_of_beggars):
        current_sum += money_list[index]
    beggars_list.append(current_sum)
    starting_index += 1
print(beggars_list)