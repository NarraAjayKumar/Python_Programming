#Write a program to generate a multiplication table of a number.
n = int(input("Enter a number:"))
for i in range(1,10 + 1):
    print(f"{n} X {i} = {n * i}")