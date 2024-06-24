string_input = input()
#numbered_list = string_input.split()
#numbered_list = list(map(int, numbered_list))
#comprehention:
numbered_list = [int(x) for x in string_input.split()]
reversed_list = [-x for x in numbered_list]
print(reversed_list)