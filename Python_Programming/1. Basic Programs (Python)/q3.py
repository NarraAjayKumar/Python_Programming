#Write a program to swap two numbers using a temporary variable.
a = int(input("Enter a number a:"))
b = int(input("Enter a number b:"))
temp = a
a = b
b = temp
print("After swapping a:",a)
print("After swapping b:",b)