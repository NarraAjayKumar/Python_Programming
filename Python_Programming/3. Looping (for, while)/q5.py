#Write a program to count the digits in a number.
n = int(input("Enter a number:"))
count = 0
if n == 0:
    count = 1
else:
    while(n!=0):
        n = n//10
        count = count + 1                                         
print(f"Number of digits are: {count}")