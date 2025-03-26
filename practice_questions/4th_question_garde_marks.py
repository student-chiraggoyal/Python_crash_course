sub1 = int(input("enter the marks of subject-1: "))
sub2 = int(input("enter the marks of subject-2: "))
sub3 = int(input("enter the marks of subject-3: "))
sub4 = int(input("enter the marks of subject-4: "))
sub5 = int(input("enter the marks of subject-5: "))
percentage = ((sub1+sub2+sub3+sub4+sub5)/500)*100
if(100>percentage>=90):
    print("A Grade")
elif(90>percentage>=80):
    print("B Grade")
elif(80>percentage>=70):
    print("C Grade")
elif(70>percentage>=60):
    print("D Grade")
elif(60>percentage>=50):
    print("E Grade")
else:
    print("you are fail")