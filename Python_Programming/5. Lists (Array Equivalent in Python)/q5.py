#Write a program to copy elements of one list to another.
n = int(input("Enter the size  of List:"))
l = []
l2 = []
for i in range(0,n):
    elements = int(input("Enter the elements{i + 1}:"))
    l.append(elements)
for i in range(0,n):
    l2.append(l[i]);
print(l2)
    
    