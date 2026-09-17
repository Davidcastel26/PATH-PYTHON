

shopping_cart = ["laptop", "vaso", "cafe", "audifonos"]
option = input("elige una opcion (1- 6)")

if option == "1":
    product = input("ingresa el nombre del producto: ")
    if product not in shopping_cart:
        shopping_cart.append(product)
        print("producto agregado")
    else:
        print("producto ya esta en el carrito")
elif option == "2":
    product = input("ingresa el nombre del producto")
    if product in shopping_cart:
        shopping_cart.remove(product)
        print("producto removed")
    else:
        print("no tienes este product")
elif option == "3":
    if len(shopping_cart) > 0:
        print('lista de compras: ')
        shopping_cart.sort()
        print(shopping_cart)
    else:
        print("la lista esta vacia")
elif option == "4":
    product = input("ingres el nombre de producto a buscar: ")
    if product in shopping_cart:
        print(f"{product} esta en la lista")
    else:
        print("producto no encontrado")
elif option == "5":
    print("total de producto en la lista: ", len(shopping_cart))
elif option == "6":
    shopping_cart.clear()
    print("lista esta vacia")
else:
    print("option no validad")