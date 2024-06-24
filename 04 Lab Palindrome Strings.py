def palindrome_verifier(initial_lst: list) -> list:
    """Creates new list with palindromes only"""
    verified_lst = []
    for element in initial_lst:
        if element == element[::-1]:
            verified_lst.append(element)
    return verified_lst


def palindrome_counter(palindrome: str, initial_lst: list) -> str:
    """Counts the given palindrome in a list"""
    counter = initial_lst.count(palindrome)
    return f'Found palindrome {counter} times'


to_be_verified = input().split()
user_palindrome = input()

print(palindrome_verifier(to_be_verified))
print(palindrome_counter(user_palindrome, to_be_verified))