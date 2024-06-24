def next_version_calculator(current: list) -> list:
    next_ver = int(''.join(current)) + 1
    print('.'.join(str(next_ver)))


current_version = input().split('.')
next_version_calculator(current_version)
