# Write a python function to check whether three given numbers can form the sides of a triangle. 

# Hint: Three numbers can be the sides of a triangle if none of the numbers are greater than or equal to the sum of the other two numbers.

def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"

    #Write your logic here
    if (num1 < num2 + num3 and num2 < num1 + num3 and num3 < num2 + num1):
        return success
    else:
        return failure
        
#Provide different values for the variables, num1, num2, num3 and test your program
num1=int(input())
num2=int(input())
num3=int(input())
form_triangle(num1, num2, num3)