mark = int(input("please enter your mark for the test: "))
if mark >= 70:
    print("Grade A")
elif mark >= 60 and mark <=69:
    print("Grade B")
elif mark >= 50 and mark <=59:
    print("Grade C")
elif mark >= 40 and mark <=49:
    print("Grade D")
elif mark >= 30 and mark <=39:
    print("Grade E")
elif mark >= 20 and mark <=29:
    print("Grade F")
else:
    print("ungradeable")
