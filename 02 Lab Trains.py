def add(num_of_people: int, train_wagon: list) -> list:
    """Adds people to the last wagon"""
    train_wagon[-1] += num_of_people
    return train_wagon


def insert(wagon_number: int, num_of_people: int, train_wagon: list) -> list:
    """Inserts people to a specified wagon"""
    train_wagon[wagon_number] += num_of_people
    return train_wagon


def leave(wagon_number: int, num_of_people: int, train_wagons: list) -> list:
    """Removes people from a specified wagon"""
    train_wagons[wagon_number] -= num_of_people
    return train_wagons


wagons_count = int(input())
lst_wagons_train = []
for i in range(wagons_count):
    lst_wagons_train.append(0)

while True:
    command = input()
    if command == 'End':
        print(lst_wagons_train)
        break
    elif 'add' in command:
        action, value = command.split()
        add(int(value), lst_wagons_train)
    else:
        action, index, value = command.split()
        if action == 'insert':
            insert(int(index), int(value), lst_wagons_train)
        else:
            leave(int(index), int(value), lst_wagons_train)
