lst_indexes = list(input().split(' '))
lst_char = list(letter for letter in input())
current_sum = 0
calculated_indexes_lst = []
secret_message = ''

for index in lst_indexes:
    for value in index:
        current_sum += int(value)
    calculated_indexes_lst.append(current_sum)
    current_sum = 0
calculated_indexes_lst = list(i % len(lst_char) for i in calculated_indexes_lst)

for char_index in calculated_indexes_lst:
    secret_message += lst_char[char_index]
    del lst_char[char_index]
    calculated_indexes_lst = list(i % len(lst_char) for i in calculated_indexes_lst)

print(secret_message)
