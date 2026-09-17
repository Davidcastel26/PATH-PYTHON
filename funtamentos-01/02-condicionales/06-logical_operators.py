# Evaluar condiciones 

# and todos los valores sean verdaderos
print(True and True) #true
print(True and False) #false
print(False and True) #false
print(False and False) #false

# or 
print(True or True) # True
print(True or False)# True 
print(False or True)# True 
print(False or False)# False

# not - negar 
print(not True) #False
print(not False) #True

# and examples 
age = 25
licesned = True

if age >= 18 and licesned:
    print("You can drive")
    
# or examples
is_student = False
membership = True

if is_student or membership:
    print("You have a special price")
    
# not examples 
is_admin = False

if not is_admin:
    print("You do not have admin privileges")