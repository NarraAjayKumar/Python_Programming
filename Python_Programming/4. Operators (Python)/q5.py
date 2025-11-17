#Write a program to find the remainder without using the modulus operator.
a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
r = a - (a//b)*b
print(r)