# this is an example of for loop
for i in range(1, 6):
    print(i)

# this is example of while loop
j=1
while(j<6):
    print(j)
    j+=1

#print "chirag" for 5 times using while loop
k=1
while(k<6):
    print("chirag")
    k+=1

#print the value of list using while loop
l=[1,2,3, "chirag", "gagan", "harshit", "ansh", "chinu", "gungun", "pushap"]
m=0
while(m<len(l)):
    print(l[m])
    m+=1

#print the values of tuple uding while loop
dd=(12,33,43,54,"chirag")
x=0
while(x<len(dd)):
    print(dd[x])
    x+=1

#print the values of string using while loop
gg="webdevelopment"
y=0
while(y<len(gg)):
    print(gg[y])
    y+=1

for a in range(4):      #range(4) ka mtlb hai ki mera loop 0 se 3 tak chalega that means---> 0,1,2,3
    print(a)

for b in range(0,100,5):   #range(start,stop,step_sizing) ka mtlb hai 0 se shuru hogi aur 99 tak jayegi lekin 5-5 k difference mein mera loop chalega
    print(b)

#print the values of list using for loop
c=[1,2,3,4,"chirag"]
for d in c:
    print(d)

#print the values of tuples using for loop
aa=(1,2,3,4,"data")
for e in aa:
    print(e)

#print the values of string using for loop
bb="chirag"
for f in bb:
    print(f)

#example of for loop with else
pp=[1,3,4,54]
for z in pp:
    print(z)
else:
    print("done")       #jab loop completely execute ho jayega tab last mein done print ho jayega

#break statement
for item in range(100):
    if(item==43):
        break           #break ka mtlb hai ki sab kuch bhula k loop mein exit maar do yahi se mera loop exit ho jayega 
    print(item)

#continue statement
for count in range(11):
    if(count==6):
        continue        #continue statement ka mtlb hai ki 6 value skip ho jayegi baaki sari value print ho jayegi
    print(count)

#example of pass statement
for i in range(45):
    pass        #pass statement ka mtlb hia ki mein is for loop pe bad mein kam krunga abbhi k liye mein isko yahi pe chod raha hu meine pass isiliye likha hai taaki ye mere code mein koi error generate na kre
my=0
while(my<31):
    print(my)
    my+=1