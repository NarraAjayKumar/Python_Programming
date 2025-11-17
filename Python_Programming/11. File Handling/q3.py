#3.	Write a program to append text to an existing file.
file = open("sample.txt","a")
text = "\n I am enjoying learning file handling in python."
file.write(text)
file.close()
print("Text appended successfully.")