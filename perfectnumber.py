# num = int(input("Enter the element :- "))
# sum = 0
# for i in range(1,num):
#     if(num%i==0):
#         sum+=i
# if(sum==num):
#     print("perfect number")
# else:
#     print("not a perfect number")


# Armstrong NUmber


num = int(input("Enter the element :- "))
s = num
b = len(str(num))

while num !=0:
    fact = num%10
    sum = sum+(fact**b)
    num//=10
if(sum==s):
    print("armstrong number")
else:
    print("not a armstrong number")