import random
n = random.randint(1, 100)
a = -1
guesses = 1
while(a!=n):
    a = int(input("guess the number "))
    if(a<n):
        print("greater number please")
        guesses += 1
    elif(a>n):
        print("lower number please")
        guesses += 1
print(f"you choose the number {n} correctly in {guesses} attempts")