# crear metodos para ver si un estudiante esta en una clase 

python_course = {'Ana', 'Luis', 'Maria', 'Pedro'}
java_course = {'Pepito', 'Pedro', 'Carlos', 'Ricardo'}

two_courses = python_course.intersection(java_course)

only_python = python_course.difference(java_course)

all_students = python_course.union(java_course)