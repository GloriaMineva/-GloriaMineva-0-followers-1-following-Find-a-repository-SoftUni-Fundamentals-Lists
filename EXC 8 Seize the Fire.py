text_input_of_fires = input()
water = int(input())
fire = list(text_input_of_fires.split('#'))
effort = 0
total_put_out_fire = 0
print('Cells:')
for cell in fire:
    if cell.startswith('High'):
        value = cell[7:]
        value = int(value)
        if 81 <= value <= 125:
            if water >= value:
                water -= value
                effort += value * 0.25
                total_put_out_fire += value
                print(f' - {value}')
            else:
                continue
        else:
            continue
    if cell.startswith('Medium'):
        value = cell[9:]
        value = int(value)
        if 51 <= value <= 80:
            if water >= value:
                water -= value
                effort += value * 0.25
                total_put_out_fire += value
                print(f' - {value}')
            else:
                continue
        else:
            continue
    if cell.startswith('Low'):
        value = cell[6:]
        value = int(value)
        if 1 <= value <= 50:
            if water >= value:
                water -= value
                effort += value * 0.25
                total_put_out_fire += value
                print(f' - {value}')
            else:
                continue
        else:
            continue
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_put_out_fire}')
