#1.	Write a program to create a file and write text into it.
file = open("sample.txt","w")
text = "Hello, I am Ajay I am Learning python file handling."
file.write(text)
file.close()
print("File created and text written successfully.")