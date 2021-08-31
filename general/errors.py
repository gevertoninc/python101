try:
    number = int(input('Enter a number: '))

    print(f'Number: {10 / number}')
except ZeroDivisionError:
    print('Impossible calculation')
except ValueError:
    print('Entrada inválida')
