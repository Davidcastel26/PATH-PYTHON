
x = [1,2,3]

type(x)
dir(x)
hasattr(x, '__len__') # devuelbe boolean para ver si existe el objeto
getattr(x, 'append') # esto manda la referencia del metodo
callable(x.append) # boolean y ver si se puede llaamar 
id(x) # esto devuelve el id del objeto