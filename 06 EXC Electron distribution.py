def electron_distributor(total_amount: int) -> list:
    shells_lst = []
    current_shell_index = 1
    while True:
        current_shell_amount = pow(current_shell_index, 2) * 2
        if total_amount > current_shell_amount:
            shells_lst.append(current_shell_amount)
            current_shell_index += 1
            total_amount -= current_shell_amount
        elif total_amount < current_shell_amount:
            shells_lst.append(total_amount)
            return shells_lst
        else:
            shells_lst.append(total_amount)
            return shells_lst




electrons_amount = int(input())
print(electron_distributor(electrons_amount))