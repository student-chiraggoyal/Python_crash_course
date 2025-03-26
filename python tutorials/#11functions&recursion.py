# this is an example of function
def avg():      #this is known as the function definition
    a=int(input("enter the value of a "))
    b=int(input("enter the value of b "))
    c=int(input("enter the value of c "))
    average=(a+b+c)/3
    print(average)
avg()       #this is known as the function call


#write a program to greet the user with the help of the function
def greet():
    name=input("enter the name of the user ")
    print("good morning",name)
greet()


#function with arguments, values and return
def goodday(name, ending):      #name aur ending yaha pe ye do arguments hai
    print("good day " + name)
    print(ending)
    return "ok"         #return ka mtlb hai ki function k pass jao aur uski value ko kisi b variable ko de do yaha pe function ki value a nam k variable k pass chali jayegi
a=goodday("chirag", "thankyou")       #yaha pe chirag aur thankyou dono function ki value hai
print(a)
# goodday("gagan", "thankyou")
# goodday("harshit", "thankyou")
# goodday("ansh", "thankyou")


#function with default argument
def koko(name, ending="thank you"):
    print("good day "+ name)
    print(ending)
koko("chirag", "wish you all the best")
# agar mein koi ending function call mein nahi dunga to by default ye us ending ko print kr dega jo meine function definition mein di hai
# jaise ki mein koi ending na du apni function call mein to output mein thank you print hoga jo ki mera by default hai lekin agar mein function call mein "wish you all the best" likh du to output mein mein "wish you all the best" hi print hoga



# ------------->>> RECURSION >>>---------------

'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 1 x 2
factorial(3) = 1 x 2 x 3
factorial(4) = 1 x 2 x 3 x 4
factorial(5) = 1 x 2 x 3 x 4 x 5
factorial(n) = n * factorial(n-1)
'''

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter the number "))
print("the factorial of the number is ",factorial(n))