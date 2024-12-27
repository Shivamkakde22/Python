import re
txt = "HEllo Sir This is Shivam"
x = re.search("/s",txt)
print(x)
# y = re.sub("[a-z]",txt)
# print(y)
z = re.findall('[A-z]',txt)
print(z)

a = re.split("[0-9]", txt)
print(a)
