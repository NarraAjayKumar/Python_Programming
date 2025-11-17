#Write a program to check whether a number is palindrome or not.
n = int(input("Enter a number:"))
rev = 0
original = n
while(n!=0):
    digit = n % 10
    rev = (rev * 10) + digit
    n = n//10
if(original == rev):
    print("Is a palindrome")
else:
    print("Is not a palindrome")
    