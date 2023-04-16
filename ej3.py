import re

string = input()
regex = r'\b(\d{4})\-(\d{2})\-(\d{2})\b'

date = re.search(regex, string)
updatedDate=r'\3.\2.\1'

updatedString = re.sub(regex, updatedDate, string)

print(updatedString)
