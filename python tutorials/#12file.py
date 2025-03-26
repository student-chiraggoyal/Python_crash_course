#f=open("file.txt")      #ye open function meri file k data ko open kr dega bydefault ye meri read mode mein hi hoti hai
# data=f.read()           #read function meri file k data ko read karega
# print(data)             #print function meri file k data ko print kr dega   
# f.close()               #close fnction meri file ko close kr dega 


# f=open("file.txt","w")
# st="hey i am a good learner and i am learning python right now"
# f.write(st)                 #is function ki help se mein apni file mein kuch bhi write kr skta hoon
# f.close()


f=open("file.txt")
lines=f.readlines()         #ye function meri file ki har ek line ko one by one read krega aur ye humesa list ki from mein read krega
print(lines, type(lines))
f.close()


f=open("file.txt")
# line1=f.readline()          #ye function meri file ki sirf first line ko read krega but ye wali line ka type string hoga
# print(line1, type(line1))

# line2=f.readline()          #ye function meri file ki sirf second line ko read krega but ye wali line ka type string hoga
# print(line2, type(line2))

# line3=f.readline()          #ye function meri file ki sirf third line ko read krega but ye wali line ka type string hoga
# print(line3, type(line3))

# line4=f.readline()          #ye function meri file ki sirf fourth line ko read krega but ye wali line ka type string hoga
# print(line4, type(line4))

# line5=f.readline()          #ye function meri file ki sirf fifth line ko read krega but ye wali line ka type string hoga
# print(line5, type(line5))

# line6=f.readline()          #ye function meri file ki sirf sixth line ko read krega but ye wali line ka type string hoga
# print(line6, type(line6))

# line7=f.readline()          #ye function meri file ki sirf sixth line ko read krega but ye wali line ka type string hoga
# print(line7, type(line7))

# the other way to print the line is with the help of the loop
line=f.readline()
while(line!=""):
    print(line)
    line=f.readline()

f.close()


f=open("file.txt")
print(f.read)
f.close()
# the same can be written using with statement like this:
with open("file.txt") as f:
    print(f.read())
# you donot have to explicitly close the file