'''a = int(input("enter the  number "))
b = int(input("enter the other number "))
print(a%b)
print(type(a))
print(a>b)
print((a+b)/2)
print(a**2)'''

'''name = input("enter the name of the user ")
print(f"good afternoon {name}")'''

# '''name = input("enter the name ")
# date = input("enter the date ")
# letter = ''' 
# Dear <|Name|>,
#     You are selected!
# <|Date|>'''
# letter = letter.replace("<|Name|>", name).replace("<|Date|>", date)
# print(letter)'''

'''string = "hello guys  my name is chirag  goyal and i am very happy today  because i am very  good"
print (string.find("  "))
print(string.replace("  ", " "))'''

'''letter = "Dear Harry,\n\tthis python course is nice.\nThanks!"
print(letter)'''

'''f1 = input("enter the fruit 1 ")
f2 = input("enter the fruit 2 ")
f3 = input("enter the fruit 3 ")
f4 = input("enter the fruit 4 ")
f5 = input("enter the fruit 5 ")
f6 = input("enter the fruit 6 ")
f7 = input("enter the fruit 7 ")
l = [f1, f2, f3, f4, f5, f6, f7]
print(l)'''

'''m1 = int(input("enter the marks "))
m2 = int(input("enter the marks "))
m3 = int(input("enter the marks "))
m4 = int(input("enter the marks "))
m5 = int(input("enter the marks "))
m6 = int(input("enter the marks "))
marks = [m1, m2, m3, m4, m5, m6]
marks.sort()
print(marks)'''

'''a = ("chirag", "chinu", "gagan")
a[2] =  4343
print(a)'''

'''l = [2, 4, 2, 3]
print(sum(l))'''

'''a = (7, 0, 8, 0, 0, 9)
print(a.count(0))'''

'''word = input("enter your word in english ")
translation = {"fan":"pankha", "chair":"kursi", "dog":"kutta", "boy":"ladka"}
print(f"the word {word} in hindi is called as {translation[word]}")'''

'''n1 = int(input("enter the number 1 "))
n2 = int(input("enter the number 2 "))
n3 = int(input("enter the number 3 "))
n4 = int(input("enter the number 4 "))
n5 = int(input("enter the number 5 "))
n6 = int(input("enter the number 6 "))
n7 = int(input("enter the number 7 "))
n8 = int(input("enter the number 8 "))
s = {n1, n2, n3, n4, n5, n6, n7, n8}
print(s, type(s))'''

# s = {18, "18"}
# print(s, type(s))/

'''s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s), s)
a = set()
print(type(a))
b = {}
print(type(b))'''

'''dictionary = {}
n1 = input("enter your name ")
l1 = input("enter your language ")
dictionary.update({n1:l1})
n2 = input("enter your name ")
l2 = input("enter your language ")
dictionary.update({n2:l2})
n3 = input("enter your name ")
l3 = input("enter your language ")
dictionary.update({n3:l3})
n4 = input("enter your name ")
l4 = input("enter your language ")
dictionary.update({n4:l4})
print(dictionary)'''

'''s = {8, 7, 12, "Harry", [1,2]}
s[4] = "chirag"
print(s)'''

'''n1 = int(input("enter the number "))
n2 = int(input("enter the number "))
n3 = int(input("enter the number "))
n4 = int(input("enter the number "))
if(n1>n2 and n1>n3 and n1>n4):
    print(f"{n1} is the greatest number")
elif(n2>n1 and n2>n3 and n2>n4):
    print(f"{n2} is th greatest number")
elif(n3>n1 and n3>n2 and n3>n4):
    print(f"{n3} is the greatest number")
else:
    print(f"{n4} is the greatest number")'''

'''n1 = int(input("enter the number "))
n2 = int(input("enter the number "))
n3 = int(input("enter the number "))
total_percentage = ((n1+n2+n3)/300)*100
if (total_percentage>=40 and n1>=33 and n2>=33 and n3>=33):
    print("you are pass")
else:
    print("you are fail")'''

'''p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"
comment = input("enter your comment here: ")
if (p1 in comment or p2 in comment or p3 in comment or p4 in comment):
    print("this is a spam")
else:
    print("this is not a spam")'''

'''username = input("enter your username: ")
if(len(username)>10):
    print("more than 10 characters")
elif(len(username)<10):
    print("less than 10 characters")
else:
    print("equal to the 10 characters")'''

'''given_list = ["chirag", "gagan", "harshit", "ansh"]
name = input("enter your name: ")
if(name in given_list):
    print("present")
else:
    print("absent")'''

'''n1 = int(input("enter the number "))
n2 = int(input("enter the number "))
n3 = int(input("enter the number "))
total_percentage = ((n1+n2+n3)/300)*100
if (total_percentage<=100 and total_percentage>90):
    print("excellent grade")
elif (total_percentage<=90 and total_percentage>80):
    print("A grade")
elif (total_percentage<=80 and total_percentage>70):
    print("B grade")
elif (total_percentage<=70 and total_percentage>60):
    print("C grade")
elif(total_percentage<=60 and total_percentage>50):
    print("D grade")
else:
    print("you are fail")'''

'''post = input("enter your post")
if("harry" in post):
    print("this post is talking about harry")
else:
    print("no! this is not about harry")'''

'''n = int(input("enter the number "))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")'''

'''l = ["Harry", "Soham", "Sachin", "Rahul"]
for item in l:
    if item.startswith("S"):
        print("good morning" + item)'''

'''n = int(input("enter the number "))
i = 1
while(i<=10):
    print(f"{n} x {i} = {n*i}")
    i+=1'''

'''n = int(input("enter the number "))
for i in range(2,n):
    if(n%i==0):
        print(f"{n} is a composite number")
        break
else:
    print(f"{n} is a prime number")'''

'''n = int(input("enter the number "))
i = 1
sum = 0
while(i<=n):
    sum+=i
    i+=1
print(f"the sum of first {n} natural numbers is {sum}")'''

'''n = int(input("enter the number "))
fact = 1
for i in range(1,n+1):
    fact*=i
print(fact)'''

'''n = int(input("enter the number "))
i = 1
fact = 1
while(i<=n):
    fact*=i
    i+=1
print(fact)'''

'''
  *
 ***
***** 
'''
'''n = int(input("enter the number "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")'''

'''
*
**
***
'''
'''n = int(input("enter the number "))
for i in range(1,n+1):
    print("*"*(i),end="")
    print("")'''

'''
* * *
*   * for n = 3
* * *
'''
'''n = int(input("enter the number "))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n)
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
        print("")'''

'''n = int(input("enter the number "))
for i in range(1,11):
    print(f"{n} x {11 - i} = {n*(11-i)}")'''

'''def greatest():
    n1 = int(input("enter the first number "))
    n2 = int(input("enter the second number "))
    n3 = int(input("enter the third number "))
    if(n1>n2 and n1>n3):
        print(f"{n1} is the greataest")
    elif(n2>n1 and n2>n3):
        print(f"{n2} is the greatest")
    else:
        print(f"{n3} is the greatest")
    return
greatest()'''

'''def temp(c):
    return c*(9/5)+32
c = int(input("enter the temp in celsius "))
f = temp(c)
print(f)'''

'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5
sum(n) = 1 + 2 + 3 + 4 + 5 + 6......... + (n-1) + n
sum(n) = sum(n-1) + n
'''
'''def sum(n):
    if(n==1):
        return 1
    else:
        return (sum(n-1) + n)
n = int(input("enter the number "))
print(sum(n))'''

'''
***
** - for n = 3
*
'''
'''def pattern(n):
    for i in range(1,n+1):
        print("*"*(n+1 - i))
n = int(input("enter the number "))
pattern(n)'''

'''def conversion(i):
    cm = i*2.54
    return cm
i = int(input("enter the value in inches "))
print(conversion(i))'''

'''def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
n = int(input("enter the number "))
table(n)'''

'''def remove(l, word):
    n = []
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n
l = ["chirag", "chinu", "chirayu"]
print(remove(l, "chi"))'''

'''
0 for stone
1 for paper
2 for secissor
'''
'''import random
def game():
    print("you are playing the game............")
    choice = {"stone":0, "paper":1, "secissor":2}
    n = input("enter your choice ")
    my_choice = choice[n]
    computer = random.choice([0,1,2])
    reverse_choice = {0:"stone", 1:"paper", 2:"secissor"}
    print("you choose", reverse_choice[my_choice])
    print("computer choose", reverse_choice[computer])
    if(my_choice == computer):
        print("it's a draw match")
    elif(my_choice == 0 and computer == 1):
        print("you loose")
    elif(my_choice == 0 and computer == 2):
        print("you win")
    elif(my_choice == 1 and computer == 0):
        print("you win")
    elif(my_choice == 1 and computer == 2):
        print("you loose")
    elif(my_choice == 2 and computer == 0):
        print("you loose")
    elif(my_choice == 2 and computer == 1):
        print("you win")
    else:
        print("invalid input")
    return n
game()'''

'''with open("poem.txt") as f:
    content = f.read()
if "twinkle" in content:
    print("present")
else:
    print("absent")'''

'''words = ["donkey", "twinkle", "star", "billu", "high"]
with open("file.txt") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "#"*len(word))
with open("file.txt", "w") as f:
    f.write(content)'''

'''with open("log.txt") as f:
    content = f.read()
if ("python" in content):
    print("present")
else:
    print("absent")'''

'''with open("log.txt") as f:
    lines = f.readlines()
lineno = 1 
for line in lines:
    if ("python" in line):
        print("python is present in the line", lineno)
        break
    lineno+=1
else:
    print("python is absent")'''

'''with open("log.txt") as f:
    content = f.read()
with open("log_copy.txt", "w") as f:
    f.write(content)'''

'''with open("log.txt") as f:
    content1 = f.read()
with open("log_copy.txt") as f:
    content2 = f.read()
if(content1==content2):
    print("files are identical")
else:
    print("files are not identical")'''

'''with open("log_copy.txt", "w") as f:
    f.write(" ")'''

'''import random
def game():
    print("you are playing the game........")
    score = random.randint(1,61)
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if hiscore!= "":
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print("your score is",score)
    if(score>hiscore):
        with open("hiscore.txt","w") as f:
            f.write(str(score))
    return score
game()'''

'''def generate_table(n):
    table = ""
    for i in range(1,11):
        table += (f"{n} x {i} = {n*i}\n")
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)
    return
for i in range(2,21):
    generate_table(i)'''

'''class employee():
    company = "microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode
c = employee("chirag", 5874854, 232334)
print(c.name, c.salary, c.pincode)
g = employee("gagan", 6763767, 677676)
print(g.name, g.salary, g.pincode) '''

'''class calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"the square of the {self.n} is {self.n*self.n}")
    def cube(self):
        print(f"the cube of the {self.n} is {self.n*self.n*self.n}")
    def square_root(self):
        print(f"the square root of the {self.n} is {self.n**1/2}")
    @staticmethod
    def hello():
        print("hello world")
a = calculator(4)
a.hello()
a.square()
a.cube()
a.square_root()'''

'''class demo():
    a = 4
o = demo()
print(o.a)
o.a = 7
print(o.a)
print(demo.a)'''

'''from random import randint
class train():
    def __init__(self, trainno):
        self.trainno = trainno
    def booking_status(self, fro, to):
        print(f"{self.trainno} was booked successfully from {fro} to {to}")
    def get_status(self, fro, to):
        print(f"{self.trainno} was running on time from {fro} to {to}")
    def fare_information(self, fro, to):
        print(f"the fare of the trainno {self.trainno} is {randint(343, 5555)} from {fro} to {to}")
    @staticmethod
    def greet():
        print("welcome to the indian railways!!")
t = train(674667)
t.greet()
t.booking_status("jammu", "goa")
t.get_status("jammu", "goa")
t.fare_information("jammu", "goa")'''

'''class twodvector():
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def show(self):
        print(f"{self.i}i + {self.j}j")
class threedvector(twodvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    def showw(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")
a = twodvector(1, 2)
a.show()
b = threedvector(3, 4, 5)
b.showw()'''

'''class animal():
    pass
class pet(animal):
    pass
class dog(pet):
    @staticmethod
    def bark():
        print("bow bow")
a = dog()
a.bark()'''

'''class employee():
    salary = 234
    increment = 20
    @property
    def salaryafterincrement(self):
        return (self.increment/100)*self.salary + self.salary
    @salaryafterincrement.setter
    def salaryafterincrement(self, salary):
        self.increment = ((salary/self.salary) - 1)*100
a = employee()
print(a.salaryafterincrement)
a.salaryafterincrement = 280
print(a.increment)'''

'''class complex():
    def __init__(self, r, i):
        self.r = r
        self.i = i
    def __add__(self, c2):
        return complex(self.r + c2.r, self.i + c2.i)
    def __mul__(self, c2):
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return complex(real_part, imag_part)
    def __str__(self):
        return f"{self.r} + {self.i}i"
c1 = complex(1, 3)
c2 = complex(4, 5)
print(c1 + c2)
print(c1 * c2)'''

'''class vector():
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    def __add__(self, v2):
        return vector(self.i+v2.i, self.j+v2.j, self.k+v2.k)
    def __mul__(self, v2):
        return (self.i*v2.i + self.j*v2.j + self.k*v2.k)
    def __str__(self) -> str:
        return f"vector({self.i}, {self.j}, {self.k})"
v1 = vector(1, 2, 3)
v2 = vector(3, 4, 5)
print(v1+v2)
print(v1*v2)'''

'''class vector():
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    def __str__(self):
        return f"vector({self.i}i + {self.j}j +  {self.k}k)"
c1 = vector(1, 2, 3)
print(c1)'''

'''class vector():
    def __init__(self, l):
        self.l = l
    def __len__(self):
        return len(self.l)
v1 = vector([1, 3, 4])
print(len(v1))'''

'''import random
n = random.randint(1, 100)
a = -1
guess = 1
while(a!= n):
    a = int(input("enter the number "))
    if(n>a):
        print("higher number please")
        guess+=1
    elif(n<a):
        print("lower number please")
        guess+=1
print(f"you guess right in {guess} attempts")'''

'''try:
    with open("file1.txt") as f:
        print(f.read())
except Exception as e:
    print(e)
try:
    with open("file2.txt") as f:
        print(f.read())
except Exception as e:
    print(e)
try:
    with open("file3.txt") as f:
        print(f.read())
except Exception as e:
    print(e)'''

'''l = ["chirag", "gagan", "harshit", "ansh", "gungun", "chinu", "kaka", "bhagu", "barkha"]
for index, item in enumerate (l):
    if index==2 or index==4 or index==6:
        print(item)'''

'''n = int(input("enter the number "))
table = [i*n for i in range(1,11)]
print(table)'''

'''try:
    a = int(input("enter a number "))
    b = int(input("enter b number "))
    print(a/b)
except ZeroDivisionError as e:
    print("infinite")'''

'''n = int(input("enter a number "))
table = [n*i for i in range(1,11)]
with open ("tables.txt", "a") as f:
    f.write(str(table) + "\n")'''