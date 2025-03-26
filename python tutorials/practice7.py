'''class programmers:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode
c = programmers("chirag", 300000000, 127306)
print(c.name, c.salary, c.pincode, c.company)
a = programmers("asnh", 300043, 143234)
print(a.name, a.salary, a.pincode, a.company)
g = programmers("gagan", 300044500, 545465)
print(g.name, g.salary, g.pincode, g.company)
k = programmers("kaka", 67437647, 758487)
print(k.name, k.salary, k.pincode, k.company)
b = programmers("bhagu", 746763546, 657465)
print(b.name, b.salary, b.pincode, b.company)
r = programmers("riya", 67367463, 567776)
print(r.name, r.salary, r.pincode, r.company)'''


'''class calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print("the square of the number is",self.n*self.n)
    def cube(self):
        print("the cube of the number is",self.n*self.n*self.n)
    def squareroot(self):
        print("the square root of the number is",self.n**1/2)
a = calculator(4)
a.square()
a.cube()
a.squareroot()'''


'''class demo:
    a=4
o = demo()
print(o.a)      #prints the class attribute because instance attribute is not present
o.a=0           #instance attribute is set
print(o.a)      #prints the instance attribute because instance attribute is present
print(demo.a)    # prints the class attribute'''


'''class calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print("the square of the number is",self.n*self.n)
    def cube(self):
        print("the cube of the number is",self.n*self.n*self.n)
    def squareroot(self):
        print("the square root of the number is",self.n**1/2)
    @staticmethod
    def hello():
        print("hello world!")
a = calculator(4)
a.hello()
a.square()
a.cube()
a.squareroot()'''


'''from random import randint
class train:
    def __init__(self, trainno):
        self.trainno = trainno

    def book(self, fro, to):
        print("ticket is booked successfully and train no is",self.trainno,"from",fro,"to",to)

    def getstatus(self):
        print("train no",self.trainno,"is running on time")

    def getfare(self, fro, to):
        print("ticket fare in train no",self.trainno,"from",fro,"to",to,"is",randint(222,22222))

    @staticmethod
    def greet():
        print("welcome to the indian railways")

t = train(43324)
t.greet()
t.book("delhi","jammu")
t.getstatus()
t.getfare("delhi","jammu")'''




'''class twodvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"the vector is {self.i}i + {self.j}j")

class threedvector(twodvector):
    def __init__(self, i , j , k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"the vector is {self.i}i + {self.j}j + {self.k}k")

a = twodvector(1, 2)
a.show()
b = threedvector(1, 2, 3)
b.show()'''


'''class animals:
    pass
class pet(animals):
    pass
class dog(pet):
    @staticmethod
    def bark():
        print("bow! bow!")

d = dog
d.bark()''' 


'''class employee:
    salary = 234
    increment = 20
    @property
    def salaryafterincrement(self):
        return self.salary + self.salary * (self.increment/100)
    @salaryafterincrement.setter
    def salaryafterincrement(self, salary):
        self.increment = ((salary/self.salary) - 1)*100
e = employee()
print(e.salaryafterincrement)
e.salaryafterincrement = 280
print(e.increment)'''


''''class complex:
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
    
c1 = complex(1, 2)
c2 = complex(3, 4)
print(c1 + c2) 
print(c1 * c2)'''



'''class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result
    
    def __str__(self):
        return f"vector({self.x}, {self.y}, {self.z})"
    
v1 = vector(1, 2, 3)
v2 = vector(4, 5, 6)
v3 = vector(7, 8, 9)

print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)

print(v2 + v3)
print(v2 * v3)'''



'''class vector:
    def __init__(self, l):
        self.l = l

    def __len__(self):
        return len(self.l)
    
v1 = vector([1, 2, 3])
print(len(v1))'''