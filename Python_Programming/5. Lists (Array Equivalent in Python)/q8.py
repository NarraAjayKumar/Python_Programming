#Write a program to perform Binary Search.
n = int(input("Enter the size  of List:"))
l = []
flag = 0
for i in range(0,n):
    elements = int(input(f"Enter the elements{i + 1}:"))
    l.append(elements)
key = int(input("Enter the Key Element:"))
st = 0
ei = n - 1
while(st<=ei):
    mid = (st + ei)//2
    if(l[mid] == key):
        print(f"Key found at index{mid}")
        flag = 1
        break
    if(l[mid]>key):
        ei = mid - 1
    else:
        st = mid + 1
if(flag == 0):
    print("Key not Found")

       
    
    