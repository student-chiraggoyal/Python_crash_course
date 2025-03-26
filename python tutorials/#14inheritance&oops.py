# ek traika to mere pass ye hai ki mein sari alag alag class bana loo lekin dikkat ye aayegi ki agr mujhe kuch change karna hua to mujhe sari classes mein change krna pdega jisse chances of error jyada ho jayege

class employees:
    company = "itc"
    def show(self):
        print(f"the name of the employee is {self.name} and the salary is {self.salary}")

# instead of doing this
'''class programmer:
    company = "itc infotech"
    def show(self):
        print(f"the name of the employee is {self.name} and the salary is {self.salary}")

    def showlanguage(self):
        print(f"the name is {self.name} and he is good with {self.language} language")'''


# i will do this with inheritance
# iska mtlb hai ki employees wali class ki to sari details mere pass fetch ho hi jayegi apne aap lekin agr mujhe kuch aur alag se add krna hua ek nai class mein to mein eise add kr skta hu 

# mtlb jo meine programmer nam ki nai class bnayi hai uski to details rahegi hi lekin sath sath mein jo mein extra add krunga wo bhi add ho jayega 

# agar mein employee wali class mein kuch change krunga to wo automatically programmer wali class mein bhi update ho jayega

# this is example of inheritance isko derived class bhi bolte hai and ye "single inheritance" ka example hai 

class programmer(employees):
    company = "itc infortech"
    def showlanguage(self):
        print(f"the name is {self.name} and he is good with {self.language} language")


a = employees()
b = programmer()
print(a.company, b.company)



# ---------> EXAMPLE OF MULTIPLE INHERITANCE <------------

class employees:
    company = "itc"
    name = "default name"
    def show(self):
        print(f"the name of the employee is {self.name} and the company is {self.company}")

class coder:
    language = "python"
    def printlanguages(self):
        print(f"out of all the languages here is your language {self.language}")

class programmer(employees, coder):
    company = "itc infortech"
    def showlanguage(self):
        print(f"the name is {self.company} and he is good with {self.language} language")

a = employees()
b = programmer()

b.show()
b.printlanguages()
b.showlanguage()


# ---------> EXAMPLE OF MULTIlevel INHERITANCE <------------

class doremon:
    a = 1
class sinchan(doremon):
    b = 2
class nobita(sinchan):
    c = 3

doremonkpapa = doremon()
print(doremonkpapa.a)       # prints the a attribute
# print(doremonkpapa.b)      shows an error as there is no b attribute in doremon class

sinchankpapa = sinchan()
print(sinchankpapa.a)
print(sinchankpapa.b)
# print(sinchankpapa.c)       shows an error as there is no c attribute in sinchan class

nobitakpapa = nobita()
print(nobitakpapa.a)
print(nobitakpapa.b)
print(nobitakpapa.c)


# ---------> EXAMPLE OF SUPER METHOD <------------

# isme doremon ka constructor sirf doremon mein hi print hoga, sinchan ka constructor sinchan mein print hoga, aur nobita ka constructor nobita mein hi print hoga

class doremon:
    def __init__(self):
        print("constructor of doremon")
    a = 1

class sinchan(doremon):
    def __init__(self):
        super().__init__()
        print("constructor of sinchan")
    b = 2

# lekin mein ye chahta hu ki doremon aur sinchan ka constructor nobita mein bhi print ho

class nobita(sinchan):
    def __init__(self):
        super().__init__()           # lekin mein ye chahta hu ki doremon aur sinchan ka constructor nobita mein bhi print ho
        print("constructor of nobita")
    c = 3

doremonkpapa = doremon()
print(doremonkpapa.a) 

sinchankpapa = sinchan()
print(sinchankpapa.a)
print(sinchankpapa.b)

nobitakpapa = nobita()
print(nobitakpapa.a)
print(nobitakpapa.b)
print(nobitakpapa.c)


# class decoraters
# iska answer dekha jaye to 45 aana chhiye lekin iska answer 1 aayega kyuki isme class method lagaya hai aur self ki jagah cls likha hai
class hattori:
    a = 1
    @classmethod
    def show(cls):
        print(f"the class attribute of a is {cls.a}")
e = hattori()
e.a = 45
e.show()


# property decoraters
class jian:
    a = 1

    @classmethod
    def show(cls):
        print("the class attribute of a is",cls.a)

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
    
e = jian()
e.a = 45

e.name = "chirag goyal"
print(e.fname, e.lname)

e.show()



# operator overloading
class number:
    def __init__(self, n):
        self.n = n
    def __add__(self, num):
        return self.n + num.n
n = number(1)
m = number(2)
print(n + m)