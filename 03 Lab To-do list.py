def notes_in_to_to_list(index: int, action: str, notes_lst: list) -> list:
    """Use pop and insert to arrange notes in a to-do list"""
    notes_lst.pop(index - 1)
    notes_lst.insert(index - 1, action)
    return notes_lst


to_do_list = [0] * 10
while True:
    command = input()
    if command == 'End':
        break
    priority, note = command.split('-')
    priority = int(priority)
    notes_in_to_to_list(priority, note, to_do_list)

to_do_list = list(filter(lambda a: a != 0, to_do_list))
# while 0 in to_do_list:
#     to_do_list.remove(0)
print(to_do_list)
