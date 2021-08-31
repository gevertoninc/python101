people = ['Me', 'Myself', 'I']

print(f'Friends: {people}')
print(f'Last friends: {people[1:]}')
print(f'First friends: {people[:2]}')
print(f'Mid friend: {people[1]}')

otherPeople = ['Jack', 'Daniel']

people.extend(otherPeople)

print(f'Friends and enemies: {people}')

people.append('James')

print(f'One more person: {people}')

people.remove('Me')

print(f'One less person: {people}')

people.pop()

print(f'And one less person: {people}')

people.sort()

print(f'Sorted people: {people}')

people.reverse()

print(f'Reversed people: {people}')

print(f'Index of jack: {people.index("Jack")}')

people.clear()

print(f'Cleared people: {people}')
