rooms_count = int(input())
counter_chairs_left = 0
couter_rooms = 0
for i in range(rooms_count):
    available_chairs, needed_chairs = input().split(' ')
    needed_chairs = int(needed_chairs)
    if len(available_chairs) < needed_chairs:
        print(f'{needed_chairs - len(available_chairs)} more chairs needed in room {i + 1}')

    else:
        counter_chairs_left += len(available_chairs) - needed_chairs
        couter_rooms += 1
    if couter_rooms == rooms_count:
        print(f'Game On, {counter_chairs_left} free chairs left')