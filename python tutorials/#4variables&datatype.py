# type casting
s=31
t=type(s)
print(t)

o=input("enter the value you want ")    #input ka type humesa "string" hota hai
print(type(o))

# type conversion
x="44.5"
y=float(x)
z=type(y)
print(z)


k=input("enter the value of k ")   #by default input function mein string ki value hoti hai 
l=input("enter the value of l ")
print(k+l)


m=int(input("enter the value of m "))  #isme humne specifically bta dia ki a ki value integer honi chahiye
n=int(input("enter the value of n "))
print(m+n)


# DATA TYPES 
a=int(input("enter the value of a "))
b=int(input("enter the value of b "))
c=a//b   #ye "quotient" btata hai integer datatype mein .....agr koi number float mein aaya hai to ye usko change krke integer data type mein show kra dega 
print(c)

d=a/b    #ye complete "quotient" btayega with points value...... complete quotient ki value btayega with points
print(d)

e=a%b    #ye hume "reminder" btayega
print(e)