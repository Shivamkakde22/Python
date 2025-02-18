# Write a program to check if a number is divisible by another number. 
a = int(input("Enter the first number :-"))
b= int(input("Enter the Second number :-"))

if(a%b==0):
    print(a," is divisible by",b) 
else:
    print(a,"is not divisible by",b)