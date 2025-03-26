# this is an example of string
name = "chirag"
print("good morning " + name)
print(name[0])   #iska mtlb hai indexing mtlb name wali string k ander 0 position pe jo element hai usko print krwa do and indexing starts from 0 to infinity(left to right) and -1 to minus infinity(right to left)
print(name[-4])


# multi line string k liye triple upper commas ka use krte hai
apple = '''aplle is very good
everyone should eat apple daaily
apple is healthy'''
print(apple)
print(apple[0:10:3])    #iska mtlb hai ki ye indexing meri 0 se 9 tak chalegi lekin 3-3 k gap m 


# iska mtlb ye h ki ye code apple string k ander jitne bhi characters hai un sabko ek sath print krwa dega
for character in apple:
    print(character)


names="chirag,gagan"
print(names[0:6])    #yaha pe string 0 se start hogi aur (n-1) tak chalegi
print(len(names))    #yeh wala function string ki length ko btata hai mtlb usme total kitne characters hai


#another example
fruit="mango"
len1=len(fruit)
print("mango is a", len1, "letter word")


print(fruit[0:4])
print(fruit[1:4])
print(fruit[:4])      #isme humne ye to bta dia ki hume 4 tak jana hai lekin ye ni btaya ki kaha se shuru krna hia  to ye bydefault 0 position se hi shuru hoga
print(fruit[:])       #iska mtlb hai ki bydefault meri string 0 se start hogi aur last tak jayegi to puri string show hogi output mein iski jagah mein ye bhi likh skta tha '''print(fruit[:5])'''
print(fruit[0:-3])    #iska mtlb hai ki string ki total length=5 hai , usme se -3 krna hai (5-3=2) ans aaya 2 to jo huamri indexing ki value hai wo [0:2} hai (to humari string mein 0 se leke 1 tak ke characters hi print honge)
print(fruit[0:-5])    #total length of string=5, so 5-5=0.... [0:0] isliye kuch bhi print ni hoga
print(fruit[0:-1])    #total length=5, so 5-1=4... [0:4] isiliye print hoga "MANG"
print(fruit[-1:-3])   #iska mtlb hai ki length of string=5 hai, toh 5-1=4 and 5-3=2 then mtlb ye hua ki 4 se leke 2 tak k characters ko print krwao jiska koi sense nahi banta mtlb 4 se leke 2 tak k characters kasie print ho skte hai isiliye yaaha pe kuch show ni hoga output mein...
print(fruit[-3:-1])   #total length=5, so 5-3=2 and 5-1=4 then the indexing is [2:4] so the ans is (NG)


nm="harry"
print(nm[-4:-2])      #total length=5, so 5-4=1 and 5-2=3 therefore [1:3] hence the ans is 1 to 2 tak k characters print honge ("ar")



######### STRINGS ARE IMMUTABLE ########### means its value can not be changed after its creation
panda="chirag"
print(panda.upper())   #ye function sare characters ko uppercase mein convert kr dega
print(panda.lower())   #ye function sare characters ko lowercase mein convert kr dega


system="####chirag#########"
print(system.rstrip("#"))   #rstrip removes any trailing characters from the string   aur    ye sirf end wale jitne bhi # hai sabko hi remove krega agr starting m b # lage hai to wo as it is print honge
print(system.replace("chirag", "gagan"))   #isne chirag ki jagah gagan ko print krwa dia    is string mein jaha jaha chirag hoga waha waha gagan aa jayega


tang="chirag gagan harshit ansh"   #this is an example of string lekin jaha jaha spcae honge to usko list b bol skte hai
print(tang.split(" "))    #isne meri string ko list mein convert kr dia


blogheading="inTrOductIon to dAta sCieNce"
print(blogheading.capitalize())  #meri string k first letter ko capitalize kr dega   or or or    agar koi aur letter agar capital hai meri string k ander to is function ki help se wo apne app small case mein ho jayega
print(blogheading.center(50))   #iska mtlb hai ki initial position se 50 characters dur mujhe centre mein show hoga


shambu="chirag chirag chirag gagan gagan"
print(shambu.count("chirag"))   #ye mujhe btayega ki meri string k ander chirag kitni baar aaya hai


rat="my name is mr. chirag and i am a data scientist now my pet name is chinu!!!!!!!!!!!"
print(rat.endswith("!"))   #ye mujhe btayega ki meri string ! se end ho ri h ya nahi
print(rat.find("name"))   #ye mujhe batyega ki meri string k ander sabse pehle "name" nam ka word konsi position pe hai
print(rat.find("over"))   #yaha meine eisa nam find kr liya jo meri string mein hai hi nahi to uska answer ye -1 se show krega 
print(rat.title())   #har ek word k first letter ko capital kr dega


str2="Welcome2TheWorld"
print(str2.isalnum())     #this method returns true if and only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or other punctuators are present, then it returns false.

str3="WelcOme1,"
print(str3.isalpha())    #this method returns true only if the entire string only consists of A-Z, a-z. If any other characters or punctuators or numbers(0-9) are present, then it returns false
print(str3.islower())    #ye btayega ki sare letters lower hai to true nahi h to false
print(str3.isprintable())    #agr sare letters printable hai to true print hoga nahi h to false aa jayega jaise ki \n hua to false print krwa dega
print(str3.istitle())     #ye mujhe btayega ki mera har ek word ka fisrt letter agr capital hai to true print kr dega otherwise false
print(str3.swapcase())     #ye uppercase ko lower bna dega aur lowercase ko upper case bna dega


str4="      "
print(str4.isspace())   #agr humari string k ander whitespaces h to true print hoga aab wo whitespaces tab key se b ho skte hai ya phir spcae bar se b ho skte hai


sapce="chirag is  a good  boy"
print(sapce.find("  "))
print(sapce.replace("  "," "))
#agar double space meri string mein nahi hai to ye -1 show krega
#very important----->>> isme print krne k bad jo humari original string hai wo to same hi rahegi kyuki string immutable hoti hai wo change nahi hoti hai yaha pe print function ek nai string bana dega
print(sapce)


letter='''Dear name
          you are selected!
date'''
print(letter.replace("name","chirag").replace("date","24 sep 2024"))