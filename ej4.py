import re

ent = input()
prof = r'\b(\w+)\.(\w+)@urjc\.es\b'
alu = r'\b\w\.(\w{2,})\.(\d{4})@alumnos\.urjc\.es\b'
resP = re.findall(prof, ent)
resA = re.findall(alu, ent)

for n, a in resP:
    print("profesor "+n+" apellido "+a)

for n, a in resA:
    print("alumno "+n+" matriculado en "+a)

