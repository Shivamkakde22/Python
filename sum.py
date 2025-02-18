# Write a program to calculate the sum of the first 100 natural numbers using a 
# for loop.

num = int(input("Enter the number: "))

sum = 0
for i in range(1,num):
    sum+=i
    print(sum)