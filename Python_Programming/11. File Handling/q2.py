#2.	Write a program to read text from a file.
file = open("sample.txt","r")
content = file.read()
print("Content of the file is:")
print(content)
file.close()
