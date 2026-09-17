
name = input("What is your name?: ")
age = input("When were you born?: ")
emial = input("Enter your email: ")
password = input("Enter your password: ")

future_age = 2050 - int(age)
password_length = len(password)

print(f"name: {name}, email: {emial}, you will be {future_age} in 2050 and your password is {'*' * password_length} ")
