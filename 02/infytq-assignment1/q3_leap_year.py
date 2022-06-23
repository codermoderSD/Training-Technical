# Write a code to find out if a given year is a leap year or not.
# Any year which is divisible by 4 and not by 100 are leap years. Otherwise, any year which is divisible by 400 is also a leap year.

year = int(input())

if year%4==0:
    if (year%400==0) and (year%100!=0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
else:
    print(year, "is not a leap year")