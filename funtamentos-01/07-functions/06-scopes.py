global_variable = "Soy global"

def outer_function():
    enclosing_variable = "soy enclosing"
    
    def inner_function():
        local_variable = "soy de inner function"
        
        print(global_variable)
        print(enclosing_variable)
        print(local_variable)
        
    inner_function()
    
outer_function()
 