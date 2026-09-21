
def divide_number():
    try:
        a = int(input("ingresa numero: ")) # a / b
        b = int(input("ingresa el nominador: "))

        result = a/b
        print(result)
        
        return result
    
    except ValueError:
        print("Por favor ingresa solo numeros.")
    
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")
    
    except Exception as error:
        print(type(error))
# try except 


divide_number()
