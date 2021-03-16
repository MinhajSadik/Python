ID = int(input("Type Your ID: "))
print("Please Below type in your ALl subject marks")
Bangla = int(input("Bangla: "))
Eniglish = int(input("English: "))
Math = int(input("Math: "))
Science = int(input("Science: "))
Socile = int(input("Socile: "))
Islam = int(input("Islam: "))
# if you got 32 marks, than your are fail in subject, So don't input the student id.
Total = (Bangla+Eniglish+Math+Science+Socile+Islam)
Avarage = Total/6
if (Avarage >= 80 and Avarage<100):
    print("you got A+")
elif (Avarage>33 and Avarage<39):
    print("Your grade is (D)")
elif (Avarage>40 and Avarage<49):
    print("Your grade is (C)")
elif (Avarage>50 and Avarage<59):
    print("Your grade is (B)")
elif (Avarage>60 and Avarage<69):
    print("Your grade is (A-)")
elif (Avarage>70 and Avarage<79):
    print("Your grade is (A)")
else:
    print("Your grad is (F)")

