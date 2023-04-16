import re

string=input()
regex=r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d{3}\s+(\w+)\s\d+\s---\s\[(\w+)\]\s(?:\w*\.)*(\w+)\s+:\s+(.+)'

matches=re.findall(regex, string)

for a, b, c, d in matches:
    print("\""+a+"\",\""+b+"\",\""+c+"\",\""+d+"\"")