candidates_lst = [int(element) for element in input().split()]
step_to_count = int(input())
removed_candidates = []
starting_point = 0
while candidates_lst: #!=None?
    for index in range(starting_point, len(candidates_lst), step_to_count):
        if candidates_lst[index] != None:
            removed_candidates.append(candidates_lst[index])
            candidates_lst.pop(index)
            starting_point += step_to_count



print(candidates_lst)
print(removed_candidates)