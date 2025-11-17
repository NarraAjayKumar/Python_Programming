#Write a program to find whether a number is divisible by 5 and 11 or not.
n = int(input("Enter a number:"))
if n % 5 == 0 and n % 11 == 0:
    print(f"{n} is divisable by 5 and 11")
else:
    print(f"{n} is not divisable by 5 and 11")