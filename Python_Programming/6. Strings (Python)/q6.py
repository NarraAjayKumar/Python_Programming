#Write a program to count vowels, consonants, digits, and spaces in a string.
str = input("Enter the String")
vowels = 0
consonants = 0
digits = 0
spaces = 0
for ch in str:
      if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
              vowels = vowels + 1
      elif('0'<=ch<='9'):
         digits = digits + 1
      elif(ch == ' '):
         spaces = spaces + 1
      else:
            consonants = consonants + 1
print("Vowels:",vowels) 
print("Consonants:",consonants)
print("Digits:",digits)
print("Spaces:",spaces)