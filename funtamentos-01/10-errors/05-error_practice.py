
class InvalidAgeError(Exception):
    def __init__(self, age, message="the ega should be >= 18"):
        self.age = age
        self.message = message
        super().__init__(self.message)
        
class InvalidEmailError(Exception):
    def __init__(self, email, message="the Email not valid"):
        self.email = email
        self.message = message
        super().__init__(self.message)
        
def register_user(name, age, email):
    if age < 18:
        raise InvalidAgeError(age)
    if "@" not in email or "." not in email.split("@")[-1]:
        raise InvalidEmailError(email)
    
    print(f"Usuario {name} registrado con la edad {age} and email: {email}")
    
try:
    register_user("David", 26, 'email@gmail.com')
except InvalidAgeError as e:
    print(f"Error: {e}")
except InvalidEmailError as er:
    print(f"Error: {er}")