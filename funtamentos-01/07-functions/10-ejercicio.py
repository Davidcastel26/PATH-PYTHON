# letras = "abcdefghijklmopqrstuvwxyzABCDFGHIJKLMNOPQRSTUVWXYZ"
# numeros = "0123456789"
# simbolos = "!@#$%^&*()_+{};',.<>?`"
# caracteres = letras + numeros + simbolos
# Formula simple: (item * 7 + 3 ) % len (caracteres)

# entrada: 8
# salida: pass
import string
import random

def password_generator(logintud):
    # letras = "abcdefghijklmopqrstuvwxyzABCDFGHIJKLMNOPQRSTUVWXYZ"
    # numeros = "0123456789"
    # simbolos = "!@#$%^&*()_+{};',.<>?`/"
    chars = string.ascii_letters + string.digits + string.punctuation
    password = []
    
    for item in range(logintud):
        # index = (item * 7 + 3 ) % len(chars)
        index = random.choice(chars)
        # pasword += chars[index]
        password.append(index)
        
    return ''.join(password)

length = int(input("cuantos caracteres quieres en tu pass?"))
print("you pass is: ", password_generator(length))