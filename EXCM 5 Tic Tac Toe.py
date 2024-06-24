first_line = [int(element) for element in input().split()]
second_line = [int(element) for element in input().split()]
third_line = [int(element) for element in input().split()]
tic_tac = [first_line, second_line, third_line]
for index in range(3):
    if tic_tac[index][0] == tic_tac[index][1] == tic_tac[index][2] == 1:
        print('First player won')
        break
    elif tic_tac[index][0] == tic_tac[index][1] == tic_tac[index][2] == 2:
        print('Second player won')
        break
    elif first_line[index] == second_line[index] == third_line[index] == 1:
        print('First player won')
        break
    elif first_line[index] == second_line[index] ==  third_line[index] == 2:
        print('Second player won')
        break
    elif first_line[0] == second_line[1] == third_line[2] == 1:
        print('First player won')
        break
    elif first_line[0] == second_line[1] == third_line[2] == 2:
        print('Second player won')
        break
    elif first_line[2] == second_line[1] == third_line[0] == 1:
        print('First player won')
        break
    elif first_line[2] == second_line[1] == third_line[0] == 2:
        print('Second player won')
        break
else:
    print('Draw!')











