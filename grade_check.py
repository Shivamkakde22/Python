# Write a program that takes a student's score as input and assigns a letter grade 
# (A, B, C, D, F) based on the score.

marks = float(input("Enter the marks:- "))

if(marks>90):
    print("Grade A")
elif(marks>90 and marks<75):
    print("Grade B")
elif(marks>60 and marks<75):
    print("Grade C")
else:
    print("Grade D")