# Write a program to calculate the sum of a list of numbers, skipping any negative 
# numbers using a for loop and the continue statemen
num = int(input("Enter the Number:."))
sum = 0
for i in range(1,num):
    if num > 0:
        sum+=i
        print(sum)
        continue
    else:
        print("It is a negative number")