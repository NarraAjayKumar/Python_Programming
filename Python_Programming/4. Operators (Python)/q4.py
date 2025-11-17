#Write a program to demonstrate increment and decrement logic.
a = int(input("Enter the number a:"))
b = int(input("Enter the number b:"))
#preincrement   
a += 1   
#predecrement
# In Python, there is no direct decrement operator, so we use -= 1
# to simulate decrementing the value.
# However, since Python does not have ++ or -- operators, we will just decrement b by 1.
b -= 1
print(f"Incremented value of a is:{a}")
print(f"Decremented value of b is:{b}")
#postincrement
a = a + 1
#postdecrement
b = b - 1
print(f"Incremented value of a is:{a}")
print(f"Decremented value of b is:{b}")