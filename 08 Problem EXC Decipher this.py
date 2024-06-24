def decipher(current_word: str) -> str:
    if 48 <= ord(current_word[2]) <= 57:
        ascii_code = current_word[0:3]
        current_word = list(current_word)
        del current_word[0:3]
    else:
        ascii_code = current_word[0:2]
        current_word = list(current_word)
        del current_word[0:2]
    deciphered_message = chr(int(ascii_code))
    current_word[0], current_word[-1] = current_word[-1], current_word[0]
    current_word.insert(0, deciphered_message)
    return ''.join(current_word)


first, second, third = input().split()

print(f'{decipher(first)} {decipher(second)} {decipher(third)}')


