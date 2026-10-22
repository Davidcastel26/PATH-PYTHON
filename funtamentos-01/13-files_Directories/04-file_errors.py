
try:
    with open("sinpermisos.txt", "r") as file:
        content = file.read()
        
except FileNotFoundError:
    print("File does not exist")
except PermissionError:
    print("You do not have access for this content privite")
except Exception as err:
    print(f"got an error: {err}")
    