n = int(input())
secret_word = input()
total_list = []
filtered_list = []
for i in range(n):
    sentence = input()
    total_list.append(sentence)
print(total_list)
for element in total_list:
    if secret_word in element:
        filtered_list.append(element)

print(filtered_list)


