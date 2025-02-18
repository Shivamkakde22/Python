# Write a program to find the largest of three given numbers.
a = int(input("Enter the first number :-"))
b= int(input("Enter the Second number :-"))
c = int(input("Enter the third number :-"))

if(a<b):
    print(b,"is a largest number")
elif(b<c):
    print(c,"is a largest number")
else:
    print(a,"is a largest number")