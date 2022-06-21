"""
Write a program to add two positive integers
"""

a=int(input())
b=int(input())

if(int(a)<=0 and int(b)<=0):
    print("NA")
elif(int(a)>=0 and int(b)>=0):
    print(int(a)+int(b))
else:
    print("NA")