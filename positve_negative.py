#  Write a program that determines if a given number is positive, negative, or zero.
n = int(input("Enter the number:- "))

if n<0:
    print(n,"is negative number")
elif n==0:
    print("Zero")
else:
    print(n,"is a positive number")