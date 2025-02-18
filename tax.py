# Write a program that calculates the income tax based on a person's income and tax
#  brackets.

def tax_calculate(income):
    
    tax_bracket = [
        (0,100000,0.0),
        (100001,500000,0.1),
        (500001,750000,0.2),
        (750001,float('inf'),0.3)
    ]
    tax = 0.0


    for lower,upper,rate in tax_bracket:
        if income>lower:
            taxable_income = min(income,upper)-lower
            tax += taxable_income * rate

    return tax

try:
    income = float(input("Enter the Number: "))
    if income<0:
        print("Income cannot be negative")
    else:
        tax = tax_calculate(income)
        print(f"The income tax for an income of Rs{income:.2f} is Rs.{tax:.2f}")
except ValueError:
    print("Please enter a valid number of income")