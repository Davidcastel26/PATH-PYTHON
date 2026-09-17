
letters = ['a', 'b', 'c', 'z', 'g', 'd', 'e']
print(letters)
#sort()

letters.sort()
print(letters)

# sorted() 
new_letters = sorted(letters)
print(new_letters)

# new_letters2 = letters[:] # list slicing
new_letters2 = letters.copy()
new_letters.sort()

# reverse para voltear
letters.reverse()

print(letters)