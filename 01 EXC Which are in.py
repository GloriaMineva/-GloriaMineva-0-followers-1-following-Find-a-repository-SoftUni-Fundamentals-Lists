def db_search(words: list, db_lst: list) -> list:
    matching_criteria_list = []
    for phrase in words:
        for mathing_element in db_lst:
            if phrase in mathing_element:
                matching_criteria_list.append(phrase)
                break
    return matching_criteria_list

word_to_search = input().split(', ')
words_db = input().split(', ')
print(db_search(word_to_search, words_db))




