# Write a program to calculate the square root of a number using the Babylonian method (while loop).

def babylonian_sqrt(n, tolerance=1e-6):
    if n < 0:
        raise ValueError("The number should not be negative")
    if n == 0:
        return 0
    
    guess = n / 2

    while True:
        next_guess = (guess + n / guess) / 2

        if abs(next_guess - guess) < tolerance:
            return next_guess
        
        guess = next_guess

try:
    n = int(input("Enter a positive number: "))
    result = babylonian_sqrt(n)
    print(f"The square root of {n} is {result:.6f}")
except ValueError as e:
    print(f"Invalid input: {e}")
