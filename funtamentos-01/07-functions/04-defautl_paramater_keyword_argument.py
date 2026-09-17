# parametro by default
def hello(greet="holla", name="invitado"):
    print(f"{greet}, {name}")
   
# keyword arguments 
hello(greet="hola", name="david")
hello(name="david", greet="Ciao")