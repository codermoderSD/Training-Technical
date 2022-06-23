# Write a code to find the sum of numbers divisible by 4.
# The code must allow the user to accept a number and add it to the sum if it is divisible by 4. 
# It should continue accepting numbers as long as the user wants to provide an input and should display the final sum.

choice=input("Type y to continue and n to exit: ")
sum=0

while choice=="y":
    num=int(input("Enter number: "))
    if num%4==0:
        sum+=num
    else:
        print("Number not divisible by 4")
    print("Sum:",sum)
    choice=input("Type y to continue and n to exit: ")
    

while choice=="n":
    print("Thank you")