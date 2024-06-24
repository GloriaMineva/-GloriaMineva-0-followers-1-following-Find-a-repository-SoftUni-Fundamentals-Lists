lst_of_numbers = list(int(num) for num in input().split(', '))
even_numbers_indexes = []
for index in range(len(lst_of_numbers)):
    if lst_of_numbers[index] % 2 == 0:
        even_numbers_indexes.append(index)

print(even_numbers_indexes)

