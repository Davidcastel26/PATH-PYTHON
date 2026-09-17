user = {
    'name': 'David',
    'age': '29',
    'greet': 'Hola mundo',
    'number': [1, 2, 3]
}

# get() 
print(user.get('name'))

# in 
print('name' in user)
print('age' in user)
print('Ricargo' in user.keys())
print('Ricardo' in user.value())

print(user.items())
