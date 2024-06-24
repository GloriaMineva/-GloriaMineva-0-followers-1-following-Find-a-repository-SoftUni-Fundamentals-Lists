string_input = input()
# if not string_input:
#     print('Team A - 11; Team B - 11')
#     exit()
team_A, team_B = 11, 11
red_cards = string_input.split()
red_cards = set(red_cards)    # could stay set - no need to list()
# count_B = 0
# count_A = 0
# count_A = sum(1 for i in red_cards if i.startswith('A'))
# #count_B = sum(1 for j in red_cards if j.startswith('B'))
# for j in red_cards:
#     if j.startswith('B'):
#         count_B += 1
#
# team_A -= count_A
# team_B -= count_B

for i in red_cards:
    if 'A' in i:
        team_A -= 1
    if 'B' in i:
        team_B -= 1
    if team_A < 7 or team_B < 7:
        print(f'Team A - {team_A}; Team B - {team_B}')
        print('Game was terminated')
        break
else:
    print(f'Team A - {team_A}; Team B - {team_B}')