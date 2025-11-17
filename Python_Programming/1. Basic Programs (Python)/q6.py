#Write a program to count vowels, consonants, digits, and spaces in a string
s = input("Enter a String:")
vowels = 0
consonants = 0
digits = 0
spaces = 0
for char in s:
    if char.isalpha():
        if char.lower() in 'aeiou':
            vowels+=1
        else:
            consonants+=1
    elif char.isdigit():
        digits+=1
    elif char.isspace():
        spaces+=1
print("Vowels:",vowels)
print("Consonants:",consonants)
print("Digits:",digits)     
print("Spaces:",spaces)
