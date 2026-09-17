
name = input("nombre del candidato: ")

experience = int(input("anos de experiencia: "))

skills = input("ingrese sus habilidades por comas (ej python, larable, goland, django etc.): ").split(",")

evaluate_skills = "Python" in skills or "Django" in skills

result = ""

if evaluate_skills:
    if experience >= 3:
        result = "candidato optimo"
    elif experience >= 1:
        result = "buen candidato"
    else:
        result = "posible candidato"
else:
    result = "No apto, se guardara CV para futuras ofertas"
    
    
print(f"el candidato {name} es: {result}")