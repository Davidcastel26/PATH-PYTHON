
def outer():
    enclosing_variable = "Enclosing variable"
    
    def inner():
        nonlocal enclosing_variable
        enclosing_variable = 'enclosing chiquito'
        