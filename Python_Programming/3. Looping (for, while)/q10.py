#Write a program to print Fibonacci series up to N terms.
n = int(input("Enter a number:"))
first = 0
second = 1
for i in range(1,n +1):
    print(first)
    next = first + second 
    first = second
    second = next
    
