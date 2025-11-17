#Write a program to check whether a string is palindrome or not.
str = input("Enter the String:")
rev = str[::-1]
if(str == rev):
    print("String is palindrome")
else:
    print("String is not a palindrome")