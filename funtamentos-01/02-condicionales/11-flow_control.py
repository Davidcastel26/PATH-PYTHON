# control de flujo

edad = int(input("introduce tu edad: "))

if edad < 0:
    print("La edad no puede ser negativa")
elif edad <= 12:
    print("eres un infante")
elif edad <= 17:
    print("eres un adolecente")
elif edad <= 64:
    print("eres un adulto")
else:
    print("eres un adulto mayor")
    
