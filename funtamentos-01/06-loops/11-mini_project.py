
inventory = {
    "chocolate":12,
    "gomitas": 4,
    "paleta": 9,
    "chicle": 5,
    "mexicano": 54,
    "galleta": 23,
}

cart = []

print("Welcome to my store")
print("inventario: ")

for candy, price in inventory.items():
    print(f"{candy.capitalize()} - ${price}")

while True:
    choice  = input("que dulces quieres comprar (escribe 'salir' para terminar)?").lower()
    
    if choice == "salir":
        break
    
    if choice in inventory:
        cart.append(choice)
        print(f"agregaste {choice} a tu carrito.")
    else: 
        print("ese duclce no existe")
        
total = 0
print("Tu carrito")

for candy in cart:
    print(f"{candy.capitalize()} - ${inventory[candy]}")
    total += inventory[candy]
    
print(f"total a pagar: {total}")
print(f"gracias por tu compra")