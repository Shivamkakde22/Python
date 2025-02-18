# Write a program to calculate the factorial of a given number using a for loop.
def factorial(n):
    if n == 0 or n == 1:
        return 1 

    else:
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact

    
n = int(input("Enter the number: "))

print(factorial(n))
