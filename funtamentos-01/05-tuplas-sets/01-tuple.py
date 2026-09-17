my_tuple = (1,2,3,"hola", True, 4)
print(my_tuple)
# ordenada
# inmutables
# permite duplicados
# indexadas

# pocos metodos
# count() contar cuantos elementos hay en la tupla
print(my_tuple.count(2)) #look for a value

# index() trae el indice del primer valor que encuentre
print(my_tuple.index("hola"))

# my_tuple[4] = "Mundo" #eerror no se puede editar
new_tuple = my_tuple[4]



