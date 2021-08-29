is_male = False

if is_male:
    print('Is male')
else:
    print('Is not male')

is_tall = True

if is_male or is_tall:
    print('Is male or is tall or is both')
else:
    print('Is neither male or tall')

if is_male and is_tall:
    print('Is male and is tall')
else:
    print('Is either not male or tall')

if is_male and is_tall:
    print('Is male and is tall')
elif is_male and not is_tall:
    print('Is male and is not tall')
elif not is_male and is_tall:
    print('Is not male and is tall')
else:
    print('Is not male and is not tall')
