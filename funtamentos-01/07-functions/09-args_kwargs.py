
def big_function(*args, **kwargs):
    print(args)
    print(kwargs)
    total = 0
    
    for item in kwargs.values():
        total += item
    
    return sum(args) + total
    
print(big_function(1,2,3, num1= 23, num2=43))