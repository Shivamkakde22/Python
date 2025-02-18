# Write a program to find the roots of a quadratic equation using the discriminant.
a = int(input("Enter the value of a :-"))
b = int(input("Enter the value of b :-"))
c = int(input("Enter the value of c :-"))

# Calculate the discriminant
dis = b**2 - 4*a*c

# Determine the nature of the roots
if dis > 0:
    root1 = (-b + dis**0.5) // (2*a)
    root2 = (-b - dis**0.5) // (2*a)
    print(f"The equation has two real roots: {root1} and {root2}.")
elif dis == 0:
    root = -b / (2*a)
    print(f"The equation has one real root: {root}.")
else:
    print("The equation has two imaginary roots.")
