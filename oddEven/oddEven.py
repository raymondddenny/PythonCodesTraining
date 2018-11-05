# Simple Program to check odd even number
data = int(input("please input a number : "))

if (data % 2 == 0):
    print("number that your input is even")
else:
    print("number that your input is odd")
    # to check if the input number is a multiple of 4
if (data % 4 == 0 and data !=):
    print(str(data) + " is a multiple of 4")

print("")
print("")

num = int(input("input a number : "))
check = int(input("input the check number : "))
# to check if the input number can be divided evenly with check number
if (num % check == 0):
    print("the number can be divided even with " + str(check))
else:
    print("the number can't  be divided even with " + str(check))
