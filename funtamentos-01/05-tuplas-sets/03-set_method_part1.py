# conjuntos
# add() agregar al set

my_set = {1,2,3}
my_set.add(6)

print(my_set)

# .remove() elimina un elemento pero da error si no existe
my_set.remove(2)
# my_set.remove(7) this is an error 
print(my_set)

# .discard() no marca error si no existe 
my_set.discard(3) #remove this but not error the next one
my_set.discard(3)
my_set.discard(7)

# .pop() elimina un elemento azar y lo devuelve 
print(my_set.pop())
print(my_set)