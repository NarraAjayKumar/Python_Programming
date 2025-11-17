#Write a program to sort a list in ascending order.-> i use bubble sort instead of this we merge sort time complexity is o(nlogn) is less
n = int(input("Enter the size  of List:"))
l = []
for i in range(0,n):
    elements = int(input("Enter the elements{i + 1}:"))
    l.append(elements)
for i in range(0,n):
   for j in range(i + 1,n):
       if(l[i]>l[j]):
           temp = l[i]
           l[i] = l[j]
           l[j] = temp
print(l)
    
    