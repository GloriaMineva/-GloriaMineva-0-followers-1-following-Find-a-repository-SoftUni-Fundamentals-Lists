def hit_check(battlefield, attack_row, attack_col, hits_counter):
    if battlefield[attack_row][attack_col] == 1:
        battlefield[attack_row][attack_col] = 0
        hits_counter += 1
    elif battlefield[attack_row][attack_col] > 1:
        battlefield[attack_row][attack_col] -= 1
    return hits_counter, battlefield


rows_count = int(input())
battlefield = []
hits_counter = 0
for row in range(rows_count):
    current_row = list(map(int, input().split(' ')))
    battlefield.append(current_row)
attacks = input().split(' ')
for attack in attacks:
    attack_row, attack_col = attack.split('-')
    attack_row, attack_col = int(attack_row), int(attack_col)
    hits_counter, battlefield = hit_check(battlefield, attack_row, attack_col, hits_counter)
print(hits_counter)


