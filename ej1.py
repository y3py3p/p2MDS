import re

string = input()
regex = r"\b(\d{4})\b"

sol = re.findall(regex, string)

for sols in sol:
    print(sols)

