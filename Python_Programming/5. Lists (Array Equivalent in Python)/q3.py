#Write a program to find the maximum and minimum element in a list.
n = int(input("Enter the number of elements:"))
l = []
for i in range(0,n):
    element = int(input(f"Enter element {i + 1}: "))
    l.append(element)
    min = l[0]
    max = l[0]
#display
for i in range(0,n):
    if(l[i]>max):
        max = l[i]
    if(l[i]<min):
        min = l[i]
print(max)
print(min)