#  Write a program to find and print all even numbers from 1 to 50 using a for loop and the continue statement.

for num in range(1,51):
    if num%2!=0:
        continue
    print(num)