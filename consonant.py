#   Write a program that checks if a given character is a consonant.
vowels = ["a","e","i","o","u"]
consonant = input("Enter the consonant: ")
if consonant not in vowels:
    print(consonant,"is in a list")
else:
    print("No consonant found")