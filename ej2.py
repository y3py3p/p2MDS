import re

string = input()

regex = r"\b(E|E\-|E\s)?(\d{4}(\-|\s)?[A-Z]{3})\b"
sol = re.findall(regex, string)

for sols in sol:
    print(sols[0]+sols[1])