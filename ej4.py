import re

regex = r'(\b[a-z]\.([a-z]{2,})\.(\d{4})\@alumnos\.urjc\.es\b)|(\b([a-z]{2,})\.([a-z]{2,})\@urjc\.es\b)'

string = input()
correo = re.findall(regex, string)

for sols in correo:
    if not sols[0]:
        print("profesor", sols[4], "apellido", sols[5])
    else:
        print("alumno", sols[1], "matriculado en", sols[2])
