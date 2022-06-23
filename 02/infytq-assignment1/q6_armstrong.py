# A three digit number is said to be an “Armstrong number” if the sum of the third power of its individual digits is equal to the number itself.
# Example: 371 is an Armstrong number as 371 = 3^ 3 + 7^ 3 + 1^ 3
#          407 is an Armstrong number as 407 = 4^ 3 + 0^ 3 + 7^ 3
# Write a code to check whether a given three digit number is an Armstrong number.

num = 371
temp=num
sum=0
while temp>0:
    rem=temp%10
    sum = sum + rem*rem*rem
    temp=temp//10
if sum==num:
    print(sum, "It is armstrong")
else:
    print(sum, "It is not armstrong")