def say_hi():
    print('Hi, bro')


print('Before')

say_hi()

print('After')


def say_hello(name):
    print(f'Hello, {name}')


say_hello('Geverton')


def cube(number):
    return number * number * number


print(f'Cube of 2: {cube(2)}')

cube_again = cube

print(f'Cube of 3: {cube_again(3)}')
