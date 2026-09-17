
shopping_cart = [
    'Camisas',
    'Tenis',
    'Calcetas',
    'Pantalones'
]


# [Inicio: fin] el slicing crea una lista nueva que ese le puede asignar a una variable

new_list = shopping_cart[0:2]

print(shopping_cart[0:2]) # camisas y tenis
print(shopping_cart[2:4]) #  tenis calcetas y pantalones

#mutar la listas
new_list[0] = 'Zapatos'

print(new_list)
print(shopping_cart)

#copiar una lista
# guardar en memoria shopping_cart
new_cart = shopping_cart
new_cart[0] = 'Playeras'
shopping_cart[1] = 'Zapatos'

# para hacer copia
new_cart1 = shopping_cart[:] # esto hara que copie de inicio a fin