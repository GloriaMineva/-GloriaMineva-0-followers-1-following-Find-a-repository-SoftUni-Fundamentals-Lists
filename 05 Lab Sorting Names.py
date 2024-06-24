# def length_bubble_sorter(some_lst: list) -> list:
#     is_sorted = False
#     while not is_sorted:
#         is_sorted = True
#         for index in range(len(some_lst) - 1):
#             if len(some_lst[index]) < len(some_lst[index + 1]):
#                 some_lst[index], some_lst[index + 1] = some_lst[index + 1], some_lst[index]
#                 is_sorted = False
#     return some_lst
#
#


# length_bubble_sorter(non_sorted_list)


non_sorted_list = input().split(', ')

non_sorted_list.sort()
new_list = sorted(non_sorted_list, key= lambda word: (-len(word), word))


print(new_list)