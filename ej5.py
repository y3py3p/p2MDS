import re

string = input()
regex = r'\b(?:C\/|Calle)\s([A-ZÁÉÍÓÚÑ]{1}[a-zñáéíóú]*)\,?\s+(?:n|N|n\º|N\º)?\s?(\d+)\,\s+(\d{5})\b'
street = re.findall(regex, string)

for calle in street:
    print(calle[2] + "-" + calle[0]  + "-"  + calle[1])