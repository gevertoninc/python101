months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

print(f'First month: {months[1]}')
print(f'Nonexistent month: {months.get(0)}')
print(f'Nonexistent month with default value: {months.get(0, "Invalid month number")}')
