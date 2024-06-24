both_racers_time = list(int(element) for element in input().split())
finish_line_index = len(both_racers_time) // 2 + 1
left_racer_times = both_racers_time[:(finish_line_index -1)]
right_racer_times = both_racers_time[finish_line_index:]
sum_left_racer = 0
sum_right_racer = 0
for current_time in left_racer_times:
    if current_time == 0:
        sum_left_racer *= 0.8
    else:
        sum_left_racer += current_time
for current_time in right_racer_times[::-1]:
    if current_time == 0:
        sum_right_racer *= 0.8
    else:
        sum_right_racer += current_time
if sum_left_racer > sum_right_racer:
    print(f'The winner is right with total time: {sum_right_racer:.1f}')
else:
    print(f'The winner is left with total time: {sum_left_racer:.1f}')



