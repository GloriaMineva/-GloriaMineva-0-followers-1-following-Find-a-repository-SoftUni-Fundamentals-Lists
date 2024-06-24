maze_size = int(input())
maze = []
for row in range(maze_size):
    current_row = input()
    maze.append(current_row)
maze = [list(row) for row in maze]
kate_out = False
counter_moves = 0
while not kate_out:
    if 'k' in maze[0] or 'k' in maze[-1]:
        counter_moves += 1
        print(f'Kate got out in {counter_moves} moves')
        kate_out = True
        break
    for row in range(1, maze_size - 1):
        for cell in range(1, maze_size + 1):
            if maze[row][0] == 'k' or maze[row][-1] == 'k':
                counter_moves += 1
                print(f'Kate got out in {counter_moves} moves')
                kate_out = True
                break
            elif maze[row][cell] == 'k' and maze[row][cell - 1] == ' ':
                counter_moves += 1
                maze[row][cell] = '#'
                maze[row][cell - 1] = ''
            elif maze[row][cell] == 'k' and maze[row + 1][cell] == ' ':
                counter_moves += 1
                maze[row][cell] = '#'
                maze[row + 1][cell] = 'k'
            elif maze[row][cell] == 'k' and maze[row - 1][cell] == ' ':
                counter_moves += 1
                maze[row][cell] = '#'
                maze[row - 1][cell] = 'k'
            elif maze[row][cell] == 'k' and maze[row][cell + 1] == ' ':
                counter_moves += 1
                maze[row][cell] = '#'
                maze[row][cell + 1] = 'k'
            elif (maze[row][cell] == 'k' and maze[row][cell + 1] == '#'
                  and maze[row][cell - 1] == '#'
                  and maze[row + 1][cell] == '#'
                  and maze[row - 1][cell] == '#'):
                print('Kate cannot get out')
                exit()







