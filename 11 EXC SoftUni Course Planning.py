def add(data, subject):
    if subject not in data:
        data.append(subject)


def insert(data, subject, index):
    if subject not in data:
        data.insert(index, subject)


def remove(data, subject):
    if subject in data:
        data.remove(subject)
        exercise_title = subject + '-Exercise'
        if exercise_title in data:
            data.remove(exercise_title)



def swap(data, first_subject, second_subject):
    if first_subject in data and second_subject in data:
        index1, index2 = data.index(first_subject), data.index(second_subject)
        data[index1], data[index2] = data[index2], data[index1]
        exercise_title1 = first_subject + '-Exercise'
        exercise_title2 = second_subject + '-Exercise'
        if exercise_title1 in data:
            data.remove(exercise_title1)
            data.insert(index2 + 1, exercise_title1)
        if exercise_title2 in data:
            data.remove(exercise_title2)
            data.insert(index1 + 1, exercise_title2)



def exercise(data, subject):
    exercise_title = subject + '-Exercise'
    if subject in data and exercise_title not in data:
        index_subject = data.index(subject)
        data.insert((index_subject + 1), exercise_title)
    elif subject not in data and exercise_title not in data:
        data.append(subject)
        data.append(exercise_title)



def process_commands(data:list, commands:list):
    for command in commands:
        parts = command.split(':')
        action = parts[0]
        if action == 'Add':
            subject = parts[1]
            add(data, subject)
        elif action == 'Insert':
            subject = parts[1]
            index = int(parts[2])
            insert(data, subject, index)
        elif action == 'Remove':
            subject = parts[1]
            remove(data, subject)
        elif action == 'Swap':
            first_subject = parts[1]
            second_subject = parts[2]
            swap(data, first_subject, second_subject)
        elif action == 'Exercise':
            subject = parts[1]
            exercise(data, subject)
    return data


data = input().split(', ')
commands = []
while True:
    command = input()
    if command == 'course start':
        break
    commands.append(command)

result = process_commands(data, commands)
for index in range(len(result)):
    print(f'{index + 1}.{result[index]}')
