cards_string = input()
count_of_shuffles = int(input())
cards_original = list(cards_string.split())
temp_list = cards_original
middle = len(temp_list) // 2
for shuffles in range(count_of_shuffles):
    cards_shuffle = []
    left_half = temp_list[:middle]
    right_half = temp_list[middle:]
    for i in range(middle):
        cards_shuffle.append(left_half[i])
        cards_shuffle.append(right_half[i])
    temp_list = cards_shuffle
print(cards_shuffle)