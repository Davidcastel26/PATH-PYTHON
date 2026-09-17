
def hello():
    print("hello world from function")
    
    return 2 + 2

def bye():
    print("bye from a function")
    return False
    
hello()
bye()
# if there is not return will return none
print(hello()) #none