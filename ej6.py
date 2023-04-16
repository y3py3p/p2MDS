import re

ent = input()
reg = r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d{3}\s+(\w+)\s\d+\s---\s\[(\w+)\]\s(?:\w*\.)*(\w+)\s+:\s+(.+)'


res = re.findall(reg, ent)
for a, b, c, d in res:
    print("\""+a+"\",\""+b+"\",\""+c+"\",\""+d+"\"")
