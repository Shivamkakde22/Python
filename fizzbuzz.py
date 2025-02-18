# Write a program that prints the numbers from 1 to 100. For multiples of 3, 
# print "Fizz" instead of the number. For multiples of 5, print "Buzz". For numbers 
# that are multiples of both 3 and 5, print "FizzBuzz".

num = int(input("Enter the number: "))
for i in range(1, num + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i,"= FizzBuzz")
    elif i % 3 == 0:
        print(i,"= Fizz")
    elif i % 5 == 0:
        print(i,"= Buzz")
    else:
        print(i," =Invalid Number")