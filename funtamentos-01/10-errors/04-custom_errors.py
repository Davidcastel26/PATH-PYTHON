
class InvalidAgeError(Exception):
    def __init__(self, age, message="the ega should be >= 18"):
        self.age = age
        self.message = message
        super().__init__(self.message)
        
def register_user(name, age):
    if age < 18:
        raise InvalidAgeError(age)
    print(f"Usuario {name} registrado con la edad {age}")
    
try:
    register_user("David", 26)
except InvalidAgeError as e:
    print(f"Error: {e}")
    
