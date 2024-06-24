def even_len(lst_of_words: list) -> str:
    """Use comprehension to filter the even len words"""
    even_only_list = list(word for word in lst_of_words if len(word) % 2 == 0)
    print('\n'.join(even_only_list))


data = input().split()
even_len(data)