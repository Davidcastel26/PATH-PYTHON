
tax = 16

def change_global():
    global tax
    tax = 19
    return tax

print(change_global())
print(tax)