# better to use append to new filtered list instead of remove
n = int(input())
original_list = []
for i in range(n):
    number = int(input())
    original_list.append(number)
sorting_criteria = input()
shallow_list = original_list[:]
if sorting_criteria == 'even':
    for j in range(len(shallow_list)):
        element = shallow_list[j]
        if element % 2 != 0:
            original_list.remove(element)
elif sorting_criteria == 'odd':
    for k in range(len(original_list) -1, -1, -1):
        element = original_list[k]
        if element % 2 == 0:
            original_list.remove(element)
elif sorting_criteria == 'negative':
    for l in range(len(original_list) -1, -1, -1):
        element = original_list[l]
        if element >= 0:
            original_list.remove(element)
elif sorting_criteria == 'positive':
    for m in range(len(shallow_list)):
        element = shallow_list[m]
        if element < 0:
            original_list.remove(element)
print(original_list)