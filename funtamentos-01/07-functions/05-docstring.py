# parametro by default
def hello(greet="holla", name="invitado"):
    """_summary_

    Args:
        greet (str, optional): _description_. Defaults to "holla".
        name (str, optional): _description_. Defaults to "invitado".
    """
    print(f"{greet}, {name}")
   
# keyword arguments 
hello(greet="hola", name="david")
hello(name="david", greet="Ciao")

def multiply(a:int, b:int) -> int :
    """_summary_

    Args:
        a (number): first number to be 'multiplicado'
        b (number): second number to be 'multiplicado'

    Returns:
        number: the times from the a and b numbers
    """
    return a + b

print(multiply(3,5))