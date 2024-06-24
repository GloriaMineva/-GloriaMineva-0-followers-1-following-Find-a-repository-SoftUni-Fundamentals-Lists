def vowel_remover(word: str) -> list:
    """
    Use comprehension to remove vowels (case sensitive): 'a', 'o', 'u', 'e', 'i'
    """
    filtered_lst = [letter for letter in word if letter.lower() not in ['a', 'o', 'u', 'e', 'i']]
    return ''.join(filtered_lst)


user_input = input()
print(vowel_remover(user_input))
