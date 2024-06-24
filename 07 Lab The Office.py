happiness_level = list(int(num) for num in input().split())
factor = int(input())
multiplied_level = list(map(lambda num: num * factor, happiness_level))
filtered_lst = list(filter(lambda num: num > sum(multiplied_level) / len(multiplied_level), multiplied_level))
if len(filtered_lst) >= len(happiness_level) // 2:
    print(f'Score: {len(filtered_lst)}/{len(happiness_level)}. Employees are happy!')
else:
    print(f'Score: {len(filtered_lst)}/{len(happiness_level)}. Employees are not happy!')

