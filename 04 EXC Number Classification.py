def classificator(num_list: list) -> str:
    """Use list comprehension to sort the numbers"""
    positive = [str(num) for num in num_list if num >= 0]
    negative = [str(num) for num in num_list if num < 0]
    even = [str(num) for num in num_list if num % 2 == 0]
    odd = [str(num) for num in num_list if num % 2 != 0]
    print(f'Positive: {", ".join(positive)}')
    print(f'Negative: {", ".join(negative)}')
    print(f'Even: {", ".join(even)}')
    print(f'Odd: {", ".join(odd)}')


user_data = list(map(int, input().split(', ')))
classificator(user_data)
