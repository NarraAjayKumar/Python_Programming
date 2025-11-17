#Write a program to search an element in a list (Linear Search).
n = int(input("Enter the size  of List:"))
l = []
flag = 0
for i in range(0,n):
    elements = int(input(f"Enter the elements{i + 1}:"))
    l.append(elements)
key = int(input("Enter the Key Element:"))
for i in range(0,n):
   if(l[i] == key):
       print(f"Key Found at Index:{i}")
       flag = 1
       break
if(flag == 0):
    print("Key not Found!")

       
    
    