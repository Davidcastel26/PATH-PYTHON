
with open('test.txt', mode="r") as my_file:
    print(my_file.readlines())
     
with open('test1.txt', mode="w") as my_file:
    print(my_file.write(':)'))
     
with open('test3.txt', mode="r+") as my_file:
    print(my_file.readlines())
    print(my_file.write(':)'))
    
with open('test3.txt', mode="a") as my_file:
    text = my_file.write("123")
    print(text)