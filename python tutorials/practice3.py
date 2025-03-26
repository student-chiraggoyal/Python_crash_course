#print multiplication table using for loop
'''num=int(input("enter the number "))
for i in range(1,11):
    print(num,"*",i,"=",num*i)
    i+=1'''

#print multiplication table using while loop
'''num=int(input("enter the number "))
i=1
while(i<11):
    print(num,"*",i,"=",num*i)
    i+=1'''

'''l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if(name.startswith("S")):
        print("good morning",name)'''

#check for the prime number
'''num=int(input("enter the value "))
for i in range(2, num):
    if(num%i==0):
        print("number is not prime")
        break
else:
    print("number is prime")'''

#sum of first n natural numbers
'''num=int(input("enter the number "))
i=1
sum=0
while(i<=num):
    sum+=i
    i+=1
print(sum)'''

#factorial of a given number using while loop
'''num=int(input("enter the number "))
i=1
fact=1
while(i<=num):
    fact*=i
    i+=1
print(fact)'''

#factorial of a given number using for loop
'''num=int(input("enter the number "))
fact=1
for i in range(1,num+1):
    fact*=i
    #i+=1
print(fact)'''

#print the pattern
'''
for n=3
  *           
 ***      
*****     '''
'''n=int(input("enter the number "))
for i in range(1,n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1),end="")
    print("")'''

#print the pattern
'''
*
**
***
'''
'''n=int(input("enter the number "))
for i in range(1,n+1):
    print("*"*(i),end="")
    print("")'''

#print the pattern
'''
***
* *
***
'''
'''n=int(input("enter the number "))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")'''

#print the table in reverse order
'''n=int(input("enter the number "))
for i in range(1,11):
    print(n*(11-i))
    i+=1'''