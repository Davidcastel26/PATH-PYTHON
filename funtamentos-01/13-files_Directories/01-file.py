
my_file = open('test.txt')

print(my_file.read())

# seek
my_file.seek(5)
print(my_file.read())

# this read line by line 
print(my_file.readline())

# lineas sobrantes 
print(my_file.readlines())

my_file.close() 