students = {
    "ana": [8, 7, 9],
    "luis": [6, 5, 7],
    "sofia":[10,9,10]
}

students["ricardo"] = [10, 7, 9]

name = "ana"

if name in students:
    student_grades = students[name]
    total_grade = (student_grades[0]+student_grades[1]+student_grades[2]/3)
    
    if total_grade >= 6.0:
        print(f"{name} aprobo con un promedio de: {total_grade}")
    else:
        print(f"{name} reprobo con un promedio de: {total_grade}") 
else:
    print("el suteniante no esta en la lista")