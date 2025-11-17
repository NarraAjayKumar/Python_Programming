#Write a program to calculate the grade of a student based on marks.
marks = int(input("Enter a number:"))
if marks>90 and marks<=100:
    print("O Grade")
elif marks>80 and marks<=90:
    print("A Grade")
elif marks>70 and marks<=80:
    print("B Grade")
elif marks>60 and marks<=70:
    print("B+ Grade")
elif marks>50 and marks<=60:
    print("C Grade")
elif marks>34 and marks<=50:
    print("PASS")
else:
    print("FAIL")