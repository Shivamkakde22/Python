# Write a program that determines the type of triangle 
# (equilateral, isosceles, scalene)

angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))
angle3 = int(input("Enter the third angle: "))

if(angle1==angle2==angle3 and angle1+angle2+angle3==180):
    print("Equilateral triangle")
elif(angle1==angle2 or angle2==angle3 or angle1==angle3 and angle1+angle2+angle3==180):
    print("Isosceles triangle")
elif(angle1+angle2+angle3==180):
    print("Scalene triangle")
else:
    print("Invalid Triangle type")
