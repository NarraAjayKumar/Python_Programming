#4.	Write a program to copy content from one file to another.
source_file = open("sample.txt","r")
destination_file = open("copy_sample.txt","w")
content = source_file.read()
destination_file.write(content)
source_file.close()
destination_file.close()
print("Content copied successfully from sample.txt to copy_sample.txt.")