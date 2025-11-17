#Write a program to store and display elements of a list.
n = int(input("Enter the number of elements:"))
l = []
for i in range(1,n +1):
    element = input(f"Enter element {i}: ")
    l.append(element)
#display
for i in range(1,n + 1):
    print(i)