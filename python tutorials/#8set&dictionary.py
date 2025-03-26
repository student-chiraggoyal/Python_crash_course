#<<<<<<<<<<<<<<         DICTIONARY          >>>>>>>>>>>>>>>>

#this is an example of dictionary-----> which is a list of key value pairs
marks={
    "chirag":100,
    "gagan":90,
    "harshit":80,
    "ansh":70,
}
print(marks, type(marks))
print(marks["chirag"])

#this is another example of dictionary
subject={
    1:"physics",
    2:"chemistry",
    3:"mathematics"
}
print(subject)

print(marks.items())   #is method se mujhe key value pair mil jayenge jo ki tuples ki form mein honge

print(marks.keys())    #is method se mujhe sirf keys mil jayengi jo meine dictionary bnayi hai uski 
print(subject.keys())

print(marks.values())    #is method se mujhe apni dictionary ki sari values mil jayengi
print(subject.values())


#is method se meri original dictionary change ho gyi 100 marks ki jagah aab 99 marks ho gye 
marks.update({"chirag":99,     #chirag wali key meri original dict mein pehle se thi to uski value 100 se 99 ho jayegi update hone k bad lekin
              "renuka":33})    #renuka nam ki key meri original dict mein nahi thi to update krne k bad renuka nam ki key automatically meri dictionary mein add ho jayegi    
print(marks)


'''in dono ka output same aayega
print(marks.get("chirag"))
print(marks["chirag"])'''     

#lekin agar kuch eisa hota to
#chirag2 nam ki koi key meri dictionary mein nahi hai
'''to jo mera .get wala method hai wo to "none" print kr dega 
aur jo square brackets wala method hai wo "error" return kr dega
bss dono mein yahi farak hai isiliye pehle prefrence .get wale method ko di jati hai'''
# print(marks.get("chirag2"))
# print(marks["chirag2"])


frist_dict={
    "name":"chirag",
    "age":19,
    "course":"b.tech",
    "domain":"data science"
}
print(frist_dict)
frist_dict.pop("name","not found")    #this method is used to remove a key value pair from the dictionary
print(frist_dict)
new_dict=frist_dict.copy()
print(new_dict)


#some other examples of dictionary are given below:::>>>
# Create a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Access a value
print("Name:", my_dict["name"])

# Add or update items
my_dict["email"] = "alice@example.com"
my_dict["age"] = 26  # Update existing key-value pair
print("Updated dictionary:", my_dict)

# Remove an item using pop() and handle KeyError
removed_value = my_dict.pop("city", "Not Found")
print("Removed value:", removed_value)
print("Dictionary after pop:", my_dict)

# Check if a key exists
if "name" in my_dict:
    print("Key 'name' exists in the dictionary")

# Get all keys, values, and items
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()
print("Keys:", keys)
print("Values:", values)
print("Items:", items)

# Iterating over a dictionary
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# Using get() to avoid KeyError
age = my_dict.get("age", "Not Found")
print("Age:", age)

# Merging two dictionaries
other_dict = {"country": "USA", "phone": "123-456-7890"}
my_dict.update(other_dict)
print("Merged dictionary:", my_dict)

# Clearing the dictionary
my_dict.clear()
print("Dictionary after clearing:", my_dict)

# Copying a dictionary
my_dict = {"name": "Alice", "age": 25}
new_dict = my_dict.copy()
print("Copied dictionary:", new_dict)


#<<<<<<<<<<<<<<<<       SETS        >>>>>>>>>>>>>>>
#sets are also in curly braces

a={}    #example of empty dictionary
print(type(a))

b={1,12,3}  #example of set
print(type(b))

c=set()     #example of empty set
print(type(c))

d={1,2,2,2,2,3,5,6,7,"chirag"}
d.add(5666)     #is function ki help se hum apne set k ander kuch bhi add kr skte hai
print(d, type(d))
l=len(d)        #isse hum apne set ki length bta skte hai
print(l)
e=d.remove(5666)    #is function ki help se hum apne set se kisi bhi element ko remove kr kte hai
print(d)

s1={1,2,3,4,5,6}
s2={4,5,6,7,8,9,10}
print(s1.union(s2))   #iska mtlb hai ki s1 ka union niklana hai wrt to s2
print(s1.intersection(s2))   #iska mtlb hai ki s1 ka intersection niklana hai wrt to s2

discard=s1.discard(50)
print(s1)

#difference between pop and discard----->>>>
#If the item to remove does not exist, discard() will NOT raise an error. You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
pop=s1.pop()
print(s1)

squared={x**2 for x in s1}
print(squared)

subset_check = {1, 2}.issubset(s1)      #ye mujhe btayega ki {1,2} mere original set ka subset hai ya nahi
print("\nIs {1, 2} a subset of set1?:", subset_check)

superset_check = s1.issuperset({1, 2})
print("Is set1 a superset of {1, 2}?:", superset_check)



#some other examples of set functions are-------->>>>>

# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Initial Sets:")
print("set1:", set1)
print("set2:", set2)

# Adding elements
set1.add(6)
print("\nAfter adding 6 to set1:", set1)

# Removing elements
set1.remove(6)  # Raises KeyError if element is not present
print("After removing 6 from set1:", set1)

set1.discard(10)  # Does nothing if element is not present
print("After discarding 10 from set1:", set1)

# Removing a random element
popped_element = set1.pop()  # Removes and returns a random element
print("Popped element:", popped_element)
print("After popping an element from set1:", set1)

# Union of sets
union_set = set1.union(set2)  # or set1 | set2
print("\nUnion of set1 and set2:", union_set)

# Intersection of sets
intersection_set = set1.intersection(set2)  # or set1 & set2
print("Intersection of set1 and set2:", intersection_set)

# Difference of sets
difference_set = set1.difference(set2)  # or set1 - set2
print("Difference of set1 and set2:", difference_set)

# Symmetric difference of sets
symmetric_difference_set = set1.symmetric_difference(set2)  # or set1 ^ set2
print("Symmetric difference of set1 and set2:", symmetric_difference_set)

# Subset and superset checks
subset_check = {1, 2}.issubset(set1)
print("\nIs {1, 2} a subset of set1?:", subset_check)

superset_check = set1.issuperset({1, 2})
print("Is set1 a superset of {1, 2}?:", superset_check)

# Set comprehension
squared_set = {x**2 for x in set1}
print("\nSet comprehension (squares of set1):", squared_set)

# Copying a set
set3 = set1.copy()
print("Copied set (set3):", set3)


chirag=set()
chirag.add(18)   #set k ander 18 as a integer hai
chirag.add("18")    #set k ander 18 as a string hai
print(chirag)       #result mein dono 18 aayge int wala bhi aur string wala bhi