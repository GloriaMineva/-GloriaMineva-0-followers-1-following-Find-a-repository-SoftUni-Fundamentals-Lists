text_items = input()
budget = float(input())
final_list = []
items_and_prices = text_items.split('|')
profit = 0
new_budget = 0
for i in items_and_prices:
    category, price = i.split('->')
    price = float(price)
    final_list.append(category)
    final_list.append(price)
for item in range(len(final_list)):
    if final_list[item] == 'Clothes':
        current_price = final_list[item + 1]
        if current_price < 50 and current_price < budget:
            budget -= final_list[item + 1]
            profit += current_price * 0.4
            new_price = current_price * 1.4
            new_budget += new_price
            print(f'{new_price:.2f}', end=' ')
    elif final_list[item] == 'Shoes':
        current_price = final_list[item + 1]
        if current_price < 35 and current_price < budget:
            budget -= final_list[item + 1]
            profit += current_price * 0.4
            new_price = current_price * 1.4
            new_budget += new_price
            print(f'{new_price:.2f}', end=' ')
    elif final_list[item] == 'Accessories':
        current_price = final_list[item + 1]
        if current_price < 20.50 and current_price < budget:
            budget -= final_list[item + 1]
            profit += current_price * 0.4
            new_price = current_price * 1.4
            new_budget += new_price
            print(f'{new_price:.2f}', end=' ')



print()
print(f'Profit: {profit:.2f}')
if budget + new_budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')