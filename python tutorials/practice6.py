'''def greatest(n1, n2, n3):
    if(n1>n2 and n1>n3):
        return n1
    elif(n2>n1 and n2>n3):
        return n2
    else:
        return n3
n1=int(input("enter the number 1 "))
n2=int(input("enter the number 2 "))
n3=int(input("enter the number 3 "))
print(greatest(n1, n2, n3),"is the greatest number")'''

'''def temperature(n):
    return ((9/5)*n)+32
n=int(input("enter the temperature in degree celsius "))
f=temperature(n)
print(round(f, 3),"is the temperature in degree farenheit")'''

'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5
sum(n) = 1 + 2 + 3 + 4 + 5 + ....... + (n-1) + n
sum(n) = sum(n-1) + n
'''
'''def sum(n):
    if(n==1):
        return 1
    else:
        return sum(n-1)+n
n=int(input("enter the number "))
print(sum(n),"is the sum of",n,"natural numbers")'''

'''
***
** 
*
'''
'''def pattern(n):
    if(n==0):
        return
    else:
        print("*"*n)
        pattern(n-1)
n=int(input("enter the number "))
(pattern(n))'''

'''def conversion(n):
    if (n<0):
        return "invalid"
    else:
        return n*2.54
n=int(input("enter the value in inches "))
print(conversion(n),"is the value in cm")'''

'''def remove(l, word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n
l=["chirag", "chinu", "china"]
print(remove(l, "chi"))'''

'''def table(n):
    for i in range(1,11):
        print(n*i)
n=int(input("enter the number "))
(table(n))'''


'''
1 for stone
2 for paper
3 for secissor
'''


'''import random
computer=random.choice([1, 2, 3])
youdict={"stone":1, "paper":2, "secissor":3}
mychoice=input("enter your choice ")
my=youdict[mychoice]
reverse_dict={1:"stone", 2:"paper", 3:"secissor"}
print("you choose",reverse_dict[my])
print("comuter choose",reverse_dict[computer])
if(computer==my):
    print("it's a draw match")
else:
    if(computer==1 and my==2):
        print("you win")
    elif(computer==1 and my==3):
        print("you loose")
    elif(computer==2 and my==1):
        print("you loose")
    elif(computer==2 and my==3):
        print("you win")
    elif(computer==3 and my==1):
        print("you win")
    elif(computer==3 and my==2):
        print("you loose")
    else:
        print("something went wrong")'''


'''with open("poem.txt") as f:
    content=f.read()
    if("twinkle" in content):
        print("yes! twinkle word is present in the poem")
    else:
        print("no! twinkle word is not present in the poem")'''


'''import random
def game():
    print("you are playing the game.... ")
    score=random.randint(1,60)
    with open("hiscore.txt") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print("your score is",score)
    if(score>hiscore):
        with open("hiscore.txt","w") as f:
            f.write(str(score))
    return score
game()'''


'''def generatetable(n):
    table=""
    for i in range(1,11):
        table+= f"{n} x {i} = {n*i}\n"
        with open(f"tables/table_{n}.txt","w") as f:
            f.write(table)
for i in range(2,21):
    print(generatetable(i))'''


'''word="donkey"
with open("file.txt") as f:
    content=f.read()
newcontent=content.replace(word,"####")
with open("file.txt","w") as f:
    f.write(newcontent)'''


'''words=["donkey", "billu", "scientist", "twinkle", "high"]
with open("file.txt") as f:
    content=f.read()
for word in words:
    content=content.replace(word, "#"*len(word))
with open("file.txt", "w") as f:
    f.write(content)'''


'''with open("log.txt") as f:
    lines=f.readlines()
lineno=1
for line in lines:
    if("python" in line):
        print("python is present in the line",lineno)
        break
    lineno+=1
else:
    print("python is not present")'''


'''with open("log.txt") as f:
    content=f.read()
with open("log_copy.txt", "w") as f:
    f.write(content)'''


'''with open("log.txt") as f:
    content1=f.read()
with open("log_copy.txt") as f:
    content2=f.read()
if(content1==content2):
    print("yes! these files are identical")
else:
    print("no! these files are not identical")'''


'''with open("log_copy.txt", "w") as f:
    f.write("")'''