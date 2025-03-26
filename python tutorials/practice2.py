'''dictionary={
    "fan":"pankha",
    "notebbok":"copy",
    "pen":"kalam",
    "boy":"ladka",
    "girl":"ladki"
}
name=input("enter the word in english ")
print("the translation in hindi of the word is ",dictionary[name])'''


'''num1=int(input("enter the number 1 "))
num2=int(input("enter the number 2 "))
num3=int(input("enter the number 3 "))
num4=int(input("enter the number 4 "))
num5=int(input("enter the number 5 "))
num6=int(input("enter the number 6 "))
num7=int(input("enter the number 7 "))
num8=int(input("enter the number 8 "))
s={num1, num2, num3, num4, num5, num6, num7, num8}
print(s, type(s))'''


'''set=set()
set.add(18)
set.add("18")
print(set)'''


'''s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))
print(s)'''


# s={}
# print(type(s))


'''d={}
n1=input("enter the name ")
l1=input("enter the language name ")
d.update({n1:l1})
n2=input("enter the name ")
l2=input("enter the language name ")
d.update({n2:l2})
n3=input("enter the name ")
l3=input("enter the language name ")
d.update({n3:l3})
n4=input("enter the name ")
l4=input("enter the language name ")
d.update({n4:l4})
print(d)'''
# agar do dosto k nam same hai to wo wala name aayega jo lst mein likha hua hoga kyuki dictionary usko update kr deti hai last wale function m


# s={8,7,12,"chirag",[1,2]}
# no you cannot change the value of the list in the set


'''num1=int(input("enter the number 1 "))
num2=int(input("enter the number 2 "))
num3=int(input("enter the number 3 "))
num4=int(input("enter the number 4 "))
if(num1>num2 and num1>num3 and num1>num4):
    print("greatest number is ",num1)
elif(num2>num1 and num2>num3 and num2>num4):
    print("greatest number is ",num2)
elif(num3>num1 and num3>num2 and num3>num4):
    print("greatest number is ",num3)
else:
    print("greatest number is ",num4)'''


'''sub1=int(input("enter the physics marks "))
sub2=int(input("enter the chemistry marks "))
sub3=int(input("enter the mathematics marks "))
total_percentage=(100*(sub1+sub2+sub3)/300)
if(total_percentage>=40 and sub1>=33 and sub2>=33 and sub3>=33):
    print("you are passed",total_percentage)
else:
    print("you are fail",total_percentage)'''


'''p1="make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"
name=input("enter your comment")
if(p1 in name or p2 in name or p3 in name or p4 in name):
    print("this is a spam")
else:
    print("this is not a spam")'''


'''name=input("enter the username ")
if(len(name)>10):
    print("true")
else:
    print("false")'''


'''name_list=["chirag", "gagan", "harshit", "ansh", "chinu", "gungun", "pushap"]
name=input("enter the name ")
if(name in name_list):
    print(name, "is present in the list")
else:
    print(name, "is not present in the list")'''


'''sub1=int(input("enter the marks of subject 1 "))
sub2=int(input("enter the marks of subject 2 "))
sub3=int(input("enter the marks of subject 3 "))
sub4=int(input("enter the marks of subject 4 "))
sub5=int(input("enter the marks of subject 5 "))
total_percentage=(100*(sub1+sub2+sub3+sub4+sub5)/500)
if(100>=total_percentage>=90):
    print(total_percentage,"excellent grade")
elif(90>=total_percentage>=80):
    print(total_percentage,"A grade")
elif(80>=total_percentage>=70):
    print(total_percentage,"B grade")
elif(70>=total_percentage>=60):
    print(total_percentage,"C grade")
elif(60>=total_percentage>=50):
    print(total_percentage,"D grade")
elif(total_percentage<50):
    print(total_percentage,"F grade")
else:
    print("invalid marks or grade")'''


'''post=input("write the post")
if("chirag".lower() in post.lower()):       #iska mtlb hai ki comparison k time pe chirag ko capital likho ya phir lower likho wo detect ho hi jayega
    print("this post is talking about chirag")
else:
    print("this post is not talking about chirag")'''