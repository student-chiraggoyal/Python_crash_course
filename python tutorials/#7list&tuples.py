# this is an example of list-----> list is a collection of different data types 
friends=["apple", "orange", 5, 685.565, True, "chirag"]

print(friends[0])
print(friends[2])

#lists are mutable datatype mtlb iske ander hum changes kr skte hai 
friends[0]="mango"
print(friends)
print(friends[0])
# iski bhi indexing bilkul string ki terah hi hoti hai 
print(friends[1:5])


# methods of lists

friends.append("gagan")  #append function meri list k end mein gagan ko bhi add kr dega
print(friends)

l1=[1,34,2,444,54,32,21]
l1.sort()   #sort method meri list k numbers ko ascending order mein convert kr dega
l1.reverse()    #reverse method se meri list k contents bhi reverse ho jayege
l1.insert(3,222)   #insert function ki help se hum apni list mein kisi bhi position pe new element ko add kr skte hai (jaise ki 3rd index pe 222 add ho jayega)
l1.pop(2)   #pop function ki help se 2nd index wala element meri list mein se delete ho jayega
print(l1.pop(2))   #ye function meri us value ko return(show) kra dega jo delete hua hai
l1.remove(1)    #ye function bhi list mein se kisi item ko delete krwane k liye use hota hai lekin farak bss itna hai ki remove function mein hum direct element likh dete hai jisko hume delete krwana hai lekin pop function mein hume jis element ko delete krwana hai uska index likhte hai
print(l1)






#this is an example of tuple
#tuples are immutable means the value of tuple can not be changed
b=(1,2,3)
print(type(b))

a=(1)    #this is an example of integer  
print(type(a))

c=(1,)
print(type(c))    #this is a tuple with single element

tup1=(1,2,3,4,32,342,443, False, "chirag", "gagan")
print(type(tup1))

fun=(1,2,2,2,2,3,222,34,54)
no=fun.count(2)    #ye function mujhe btayega ki mere tuple k ander kitni bar 2 likha hua hai
print(no)

i=fun.index(2)    #mere tuple k ander bht sare 2 hai to ye us 2 ka index btayega jo sabse pehle likha hua hai 
print(i)


# Creating a tuple
t = (1, 2, 3, 4, 5)

# Using common functions
print("Length:", len(t))         # Output: 5
print("Max value:", max(t))      # Output: 5
print("Min value:", min(t))      # Output: 1
print("Sum:", sum(t))            # Output: 15

# Using tuple methods
print("Index of 3:", t.index(3)) # Output: 2
print("Count of 2:", t.count(2)) # Output: 1

# Converting a list to a tuple
lst = [6, 7, 8]
new_tuple = tuple(lst)
print("New tuple:", new_tuple)   # Output: (6, 7, 8)


#concatenation of two tuples

# Define two tuples with different data types
tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)

# Concatenate the tuples
concatenated_tuple = tuple1 + tuple2

# Print the result
print(concatenated_tuple)  # Output: ('a', 'b', 'c', 1, 2, 3)



#concatenation of two tuples with nested tuples

# Define two tuples with nested tuples
tuple1 = (1, (2, 3), 4)
tuple2 = ((5, 6), 7, 8)

# Concatenate the tuples
concatenated_tuple = tuple1 + tuple2

# Print the result
print(concatenated_tuple)  # Output: (1, (2, 3), 4, (5, 6), 7, 8)
