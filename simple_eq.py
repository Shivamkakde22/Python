#  Write a program that solves a simple linear equation (e.g., ax + b = c).

def simple_equation(a,b,c):
    if a == 0:
        if b==c:
            return "Infinite solutions"
        else:
            return "No solution"
    else:
        x = (c-b)/a
        return x
    
try:
    a = int(input("Enter the value of a:"))
    b = int(input("Enter the value of b:"))
    c = int(input("Enter the value of c:"))

    result = simple_equation(a,b,c)

    if isinstance(result,str):
        print(result)
    else:
        print(f"the equation is {a}x + {b} = {c} and x = {result:.2f}.")
except ValueError:
    print("Invalid input. Please enter a valid number.") 