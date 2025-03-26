# Write a program using functions to find greatest of three numbers.
'''def greatest():
    num1=int(input("enter the first number "))
    num2=int(input("enter the second number "))
    num3=int(input("enter the third number "))
    if(num1>num2 and num1>num3):
        print(num1,"is the largest number")
    elif(num2>num1 and num2>num3):
        print(num2,"is the largest number")
    else:
        print(num3,"is the largest number")
greatest()'''

'''def greatest(num1, num2, num3):
    if(num1>num2 and num1>num3):
        print(num1,"is the largest number")
    elif(num2>num1 and num2>num3):
        print(num2,"is the largest number")
    else:
        print(num3,"is the largest number")
greatest(5, 6, 7)'''


# Write a python program using function to convert Celsius to Fahrenheit
'''def temp():
    n=int(input("enter the value of celsius "))
    f=((9/5)*n)+32
    print("the temp in farenheit is",f)
temp()'''

'''def temp(n):
    return ((9/5)*n)+32
n=int(input("enter the temp in celsius "))
c=temp(n)
print(round(c, 2),"degree farenheit")'''


# write a pyhton program of recursion to print sum of n natural numbers
'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5
sum(n) = 1 + 2 + 3 + 4 + 5 + 6 + ..... + (n-1) + n
sum(n) = sum(n-1) + n
'''
'''def sum(n):
    if(n==1):
        return 1
    else:
        return n+sum(n-1)
n=int(input("enter the number "))
print("the sum of",n,"natural numbers is",sum(n))'''


# write a python program using function to print the following pattern
'''
***
**
*
'''

'''def star(n):
    if(n==0):
        return
    else:
        print("*"*n)
        star(n-1)
n=int(input("enter the value "))
print(star(n))'''
# The print(pattern(n)) statement will print None after the pattern because the pattern function does not return any value (implicitly returns None). To avoid printing None, you can simply call the pattern function without printing its return value:

'''n=int(input("enter the number "))
for i in range(1,n+1):
    print("*"*(n+1-i),end="")
    print("")'''


# write a python function which converts inches to cm
'''def conversion(n):
    if(n==0):
        return
    else:
        return n*2.54
n=int(input("enter the value in inches "))
c=conversion(n)
print(round(c, 4),"is the answer in cm")'''


# write a python function to remove the word from th list and strip it
'''def remove(l, word):
    n=[]
    for item in l:
       if not(item==word):
           n.append(item.strip(word))
    return n
l=["chirag", "chinu", "chirayu", "chi"]
print(remove(l, "chi"))
'''


# write a python function to print multiplication table of a given number
'''def table(n):
    for i in range(1,11):
        print(n*i)
n=int(input("enter the value "))
print(table(n))'''