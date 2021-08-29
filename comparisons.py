def max_number(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2


print(f'Max number: {max_number(4, 2)}')


def max_number_v2(number1, number2):
    return number1 if number1 > number2 else number2


print(f'Max number v2: {max_number_v2(4, 8)}')
