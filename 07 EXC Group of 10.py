def decades_sorter(numbers_lst : list) -> str:
    if max(numbers_lst) % 10 == 0:
        biggest_decade = max(numbers_lst) // 10
    else:
        biggest_decade = max(numbers_lst) // 10 + 1
    current_decade_lst = []
    for decade in range(1, biggest_decade + 1):
        current_decade_lst = list(num for num in numbers_lst if (decade - 1) * 10 < num <= decade * 10)
        print(f"Group of {decade}0's: {current_decade_lst}")


user_data = list(map(int, input().split(', ')))
decades_sorter(user_data)