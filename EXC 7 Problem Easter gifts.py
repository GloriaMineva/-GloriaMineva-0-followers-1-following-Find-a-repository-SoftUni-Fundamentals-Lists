text_gifts = input()
gifts = list(text_gifts.split())
searched_gift = ''
while True:
    command = input()
    if command == 'No Money':
        break
    elif command.startswith('OutOfStock'):
        searched_gift = command[11:]
        while searched_gift in gifts:
            gifts[gifts.index(searched_gift)] = None
    elif command.startswith('Required'):
        searched_gift = command[9:]
        searched_gift = list(searched_gift.split())
        if int(searched_gift[1]) < len(gifts):
            gifts[int(searched_gift[1])] = searched_gift[0]
    elif command.startswith('JustInCase'):
        searched_gift = command[11:]
        gifts[-1] = searched_gift
gifts = ' '.join(filter(None, gifts))
print(gifts)

