# Write a program to reverse a given string using a for loop.

string = input("Enter the string: ")
rev_str = ""
for i in string:
    rev_str = i + rev_str
print(rev_str)

