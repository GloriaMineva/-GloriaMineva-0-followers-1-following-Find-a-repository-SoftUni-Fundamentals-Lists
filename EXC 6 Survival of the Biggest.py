numbers_string = input()
remover_count = int(input())
smallest_num = None
numbers_list = list(int(i) for i in numbers_string.split())
for i in range(remover_count):
    smallest_num = min(numbers_list)
    numbers_list.remove(smallest_num)
numbers_list = [str(j) for j in numbers_list]
joined_list = ', '.join(numbers_list)
print(joined_list)