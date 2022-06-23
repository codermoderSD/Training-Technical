# Write a code to find the minimum among three given numbers.
# Assume that the three numbers are always different.

num1 = input()
num2 = input()
num3 = input()

if(num1<num2) and (num1<num3):
    print(num1, "is the smallest")
elif(num2<num3):
    print(num2, "is the smallest")
else:
    print(num3, "is the smallest")