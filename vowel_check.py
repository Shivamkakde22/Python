#  Write a program that checks if a given character is a vowel.
vowels = ["a","e","i","o","u"]
vowel = input("Enter the vowel: ")
if vowel in vowels:
    print(vowel,"is in a list")
else:
    print("No vowel found")