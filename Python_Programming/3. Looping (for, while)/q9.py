#Write a program to find the sum of digits of a number.
n = int(input("Enter a number:"))
sum = 0
for i in range(0,n):
    digit = n % 10
    n = n//10
    sum = sum + digit
print(f"sum is:{sum}")