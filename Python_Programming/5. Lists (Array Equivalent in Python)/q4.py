#Write a program to count even and odd numbers in a list.
n = int(input("Enter the Size:"))
l = []
even = 0
odd = 0
for i in range(0,n):
    elements = int(input(f"Enter the Elements{i + 1}:"))
    l.append(elements)
for i in range(0,n):
    if(l[i]%2 == 0):
        even = even + 1
    else:
        odd = odd + 1
print(even)
print(odd)