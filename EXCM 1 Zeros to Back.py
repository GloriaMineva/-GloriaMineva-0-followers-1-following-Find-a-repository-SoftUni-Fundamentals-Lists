lst_numbers = list(int(i) for i in input().split(', '))
for is_zero in lst_numbers:
    if is_zero == 0:
        lst_numbers.remove(0)
        lst_numbers.append(0)
print(lst_numbers)