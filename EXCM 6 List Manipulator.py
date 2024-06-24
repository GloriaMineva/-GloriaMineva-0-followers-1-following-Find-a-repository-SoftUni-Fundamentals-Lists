lst_to_manipulate = [int(element) for element in input().split()]
command = None
while command != 'end':
    command = input()
    if command == 'max odd':
        odd_value = 0
        for element in lst_to_manipulate[::-1]:
            if element % 2 != 0 and element > odd_value:
                odd_value = element
        if odd_value != 0:
            print(lst_to_manipulate.index(odd_value))
        else:
            print('No matches')
    elif command == 'max even':
        even_value = 0
        for element in lst_to_manipulate[::-1]:
            if element % 2 == 0 and element > even_value:
                even_value = element
        if even_value != 0:
            print(lst_to_manipulate.index(even_value))
        else:
            print('No matches')
    elif command == 'min odd':
        odd_value = max(lst_to_manipulate)
        for element in lst_to_manipulate[::-1]:
            if element % 2 != 0 and element < odd_value:
                odd_value = element
        if odd_value % 2 != 0:
            print(lst_to_manipulate.index(odd_value))
        else:
            print('No matches')
    elif command == 'min even':
        even_value = max(lst_to_manipulate)
        for element in lst_to_manipulate[::-1]:
            if element % 2 == 0 and element < even_value:
                even_value = element
        if even_value % 2 == 0:
            print(lst_to_manipulate.index(even_value))
        else:
            print('No matches')
    elif 'exchange' in command:
        exchange_command, exchange_index = command.split()
        exchange_index = int(exchange_index)
        if 0 <= exchange_index < len(lst_to_manipulate):
            first_half_exchange_list = lst_to_manipulate[:(exchange_index + 1)]
            second_half_exchange_list = lst_to_manipulate[(exchange_index + 1):]
            lst_to_manipulate = second_half_exchange_list + first_half_exchange_list
        else:
            print('Invalid index')
            continue
    elif 'first' in command:
        command_value, count_value, type_of_num = command.split()
        count_value = int(count_value)
        counter = 0
        matching_criteria_list = []
        if count_value > len(lst_to_manipulate):
            print('Invalid count')
            continue
        if type_of_num == 'even':
            for element in lst_to_manipulate:
                if element % 2 == 0 and counter < count_value:
                    matching_criteria_list.append(element)
                    counter += 1
            print(matching_criteria_list)
        if type_of_num == 'odd':
            for element in lst_to_manipulate:
                if element % 2 != 0 and counter < count_value:
                    matching_criteria_list.append(element)
                    counter += 1
            print(matching_criteria_list)
    elif 'last' in command:
        command_value, count_value, type_of_num = command.split()
        count_value = int(count_value)
        counter = 0
        matching_criteria_list = []
        if count_value > len(lst_to_manipulate):
            print('Invalid count')
            continue
        if type_of_num == 'even':
            for element in lst_to_manipulate[::-1]:
                if element % 2 == 0 and counter < count_value:
                    matching_criteria_list.append(element)
                    counter += 1
            print(matching_criteria_list[::-1])
        if type_of_num == 'odd':
            for element in lst_to_manipulate[::-1]:
                if element % 2 != 0 and counter < count_value:
                    matching_criteria_list.append(element)
                    counter += 1
            print(matching_criteria_list[::-1])
print(lst_to_manipulate)

