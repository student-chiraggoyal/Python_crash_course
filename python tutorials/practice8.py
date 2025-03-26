'''try:
    with open("file1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)
try:
    with open("file2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)
try:
    with open("file3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

print("thank you")'''


'''l = [1, 2, 3, 4, 5, 6, 7, 8]
for i, item in enumerate (l):
    if i == 2 or i == 4 or i == 6:
        print(item)'''


'''n = int(input("enter the number "))
table = [n*i for i in range(1,11)]
print(table)'''


'''try:
    a = int(input("enter number a: "))
    b = int(input("enter number b: "))
    print(a/b)
except ZeroDivisionError as v:
    print("infinite")'''


'''n = int(input("enter the number: "))
table = [n*i for i in range(1,11)]
with open("tables.txt","a") as f:
    f.write(str(table) + "\n")'''


'''  run in windows powershell
1. command for create a new virtual enviroment
ANS: virtualenv <name>
for ex: virtualenv env1
for ex: virtualenv env2

2. command how to activate the virtual enviroment
ANS: .\name\Scripts\activate.ps1
for ex: .\env1\Scripts\activate.ps1
for ex: .\env2\Scripts\activate.ps1

3. command how to install packages
ANS: pip install <name>
for ex: pip install pandas

4. command to generate requirements file
ANS: pip freeze > requirements.txt

5. command to deactivate virtual enviroment
ANS: deactivate

6. command to install the packages in requirements file
ANS: pip install -r .\requirements.txt
'''


'''name = input("enter your name ")
marks = int(input("enter your marks here "))
phone_number = input("enter your phone number here ")
a = "The name of the student is {} , his marks are {} , and phone number is {}".format(name, marks, phone_number)
print(a)'''


'''l = [str(7*i) for i in range(1,11)]
join = "\n".join(l)
print(join)'''

'''l = [3, 5, 8, 10, 15, 14, 19, 25]
def divisibe(n):
    if(n%5 == 0):
        return True
    return False
a = list(filter(divisibe, l))
print(a)'''


'''from functools import reduce
l = [54, 87, 32, 98, 14]
def max(a, b):
    if(a>b):
        return a
    return b
print(reduce(max, l))'''


'''from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()'''