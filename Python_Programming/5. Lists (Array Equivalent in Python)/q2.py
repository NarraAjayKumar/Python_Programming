#Write a program to find the sum of list elements.
n = int(input("Enter the number of elements:"))
sum = 0
l = []
for i in range(0,n):
    element = int(input(f"Enter element {i + 1}: "))
    l.append(element)
#display
for i in range(0,n):
    sum = sum + l[i]
print(sum)