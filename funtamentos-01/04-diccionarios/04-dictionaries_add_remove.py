user = {
    'name': 'David',
    'age': 29,
    'greet': 'Hola mundo',
    'number': [1, 2, 3]
}

# copy()
user_copy = user.copy()

user_copy['age'] = 20

user_copy.pop('age')

# pop item removes the last item
user_copy.popitem()

# update() update a value
user_copy.update({'name':'Fernando'})

# append() 
user['skills'] = user.get('skills', [])
user['skills'].append('Python')
