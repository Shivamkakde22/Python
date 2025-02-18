string = str(input("Enter the string:"))
find_char = input("Enter the char to find:")

for index,char in enumerate(string):
    if char==find_char:
        print(f"Found '{find_char}' at index {index}")
        break

else:print(f"{find_char} is not found on a given string")
