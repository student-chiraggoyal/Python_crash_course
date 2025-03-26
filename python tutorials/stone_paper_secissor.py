import random
'''
1 for stone
2 for paper
3 for secissor
'''
computer=random.choice([1,2,3])

mydict={"stone":1, "paper":2, "secissor":3}

you=input("enter your choice ")
my=mydict[you]

reversedict={1:"stone", 2:"paper", 3:"secissor"}
print("you choose",reversedict[my])
print("computer choose",reversedict[computer])

if(computer==my):
    print("its a draw")
else:
    if(computer==1 and my==2):          # computer - my = -1
        print("you win")
    elif(computer==1 and my==3):        # computer - my = -2
        print("you loose")
    elif(computer==2 and my==1):        # computer - my = 1
        print("you loose")
    elif(computer==2 and my==3):        # computer - my = -1
        print("you win")
    elif(computer==3 and my==1):        # computer - my = 2
        print("you win")
    elif(computer==3 and my==2):        # computer - my = 1
        print("you loose")
    else:
        print("something went wrong")
    
    
    # if-elif-else ki jagah ye niche wala code bhi likh sakta hoon
    '''if((computer - my)==1 or (computer - my)==-2):
        print("you loose")
    else:
        print("you win")'''