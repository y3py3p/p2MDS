import re

ent = input()
reg = r'\b(?:C\/|Calle) ([A-ZÁÉÍÓÚÑ][a-zñáéíóú]+),? +(?:(?:N|n)º? ?)?(\d+), +(\d{5})\b'


res = re.findall(reg, ent)
for c, n, p in res:
    print(p+"-"+c+"-"+n)