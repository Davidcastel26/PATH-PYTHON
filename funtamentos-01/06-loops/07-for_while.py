# for para iterables cuando sabemos cuando terminara 
# while: no sabemos cuando terminara y necesitamos una condicion 

my_list = [1,2,3]

for item in my_list:
    print(item)
    
item = 0
while item < len(my_list):
    print(item)
    item += 1