#5.	Write a program to count the number of characters, words, and lines in a file.
file = open("sample.txt","r")
content = file.readlines()
num_lines = len(content)
num_words = 0
num_characters = 0
for line in content:
    num_characters += len(line)
    words = line.split()
    num_words += len(words)
file.close()
print("Number of lines:", num_lines)
print("Number of words:", num_words)
print("Number of characters:", num_characters)
