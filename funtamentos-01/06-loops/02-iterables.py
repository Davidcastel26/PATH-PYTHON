numbers = [1,2,3,4,5]
iterator = iter(numbers)

print(iterator)

print(next(iterator)) #iterar paso a paso
# print(next(iterat))


user = {
    "name":"david",
    "age": 26,
    "can_swim": False
}
# for item in user.values() get the values
# for item in user.items() get the kyes and values 
# and user get the key 
# item has (key and hte value)
for key, value in user.items():
    print(key, value)