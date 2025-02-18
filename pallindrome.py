# Write a program to check if a given string is a palindrome using a for loop.

string = input("Enter the string: ")
rev_str = ""
for i in string:
    rev_str = i + rev_str

if string == rev_str:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")