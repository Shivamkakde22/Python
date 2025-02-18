    # Write a program to check if a given number is a prime number.
def prime_number(num):
    for i in range(2,num):
        if(num%i==0):
            return True
        elif(num==1):
            return True
    return False

num = int(input("Enter the number: "))
if prime_number(num):
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")