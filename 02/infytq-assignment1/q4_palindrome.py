# Write a code to check whether a given number is a palindrome.
# Examples of palindrome: 121, 1331, 2332,78900987,123456654321 etc.

num = 121
temp = num
rev = 0

while num != 0:
    rem = num % 10
    rev = rev*10 + rem
    num = int(num/10)

if rev==temp:
    print("Palindrome")
else:
    print("Not palindrome")