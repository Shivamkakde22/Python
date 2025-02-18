#  Write a program to implement a simple countdown using a while loop

import time

def countdown(t):
    while t>0:
        print(t)
        time.sleep(1)
        t -=1

t = float(input("Enter the Number: "))

if t>0:
    countdown(t)
else:
    print("Enter the positive number")
