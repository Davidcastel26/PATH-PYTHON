
# while True:
    # pass
    # print("esto nunca se detendra") # loop infinito
    
    
    
counter = 1
while counter <= 5:
    print(f"Number: {counter}")
    counter += 1
else:
    print("Terminamos")
    
response = ''

while response.lower() != 'python':
    response = input("escribe python para salir: ")
print('Terminamos')