n = [1, 2, 3, 4, 5]
n = len([1, 2, 3, 4, 5])
if(n>3):
    print(f"list is too long ({n} elements, expected <=3")
# isko hum kuch is terike se bhi likh sakte hai


# example of walrus operator (:=)
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"list is too long ({n} elements, expected <=3)")
    # iska mtlb hai ki pehle ek list ko define kro phir uski length ko define kia phir uspe condition lagayi aur last mein print krwa diya


# ye programmer ko pehle hi bta denge ki function k ander kon kon se types k argumnets hai jisse program ki readbility achi ho jayegi
# Type hints are added using the colon (:) syntax for variables and the -> syntax for function return types.

# Variable type hint
age: int = 25
# Function type hints
def greeting(name: str) -> str:
    return f"Hello, {name}!"
print(greeting("Alice")) # Output: Hello, Alice!

# another example
def company(name: str) -> str:
    return f"{name}, work in microsoft"
print(company("chirag"))


# advance typing hints
# inka mainly use program ki readability ko badane k liye kia jata hai
from typing import List, Tuple, Dict, Union

numbers : List[int] = [1, 2, 3, 4, 5]   # list of integers
print(numbers)

person : Tuple[str, int] = ("chirag", 7676) # tuples of a string and an integer
print(person)

scores : Dict[str, int] = {"chirag":10, "oggy":8}   #dictionary with string keys and integer values
print(scores)

identifier : Union[int, str] = "123id"      # union type for variables that can hold string and integer values (multiple types)
print(identifier)


# example of match case
def https_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "ERROR NOT FOUND"
        case 500:
            return "internal server error"
        case _:             # by default
            return "unknown status"
print(https_status(200))
print(https_status(300))
print(https_status(404))
print(https_status(190))
print(https_status(500))


# dictionary merged
dict1 = {"chirag":1, "gagan":2}
dict2 = {"harshit":3, "ansh":4}
merged = dict1 | dict2
print(merged)


'''# open multiple files
with (
    open("file1.txt") as f1,
    open("file2.txt") as f2
):
    # under process'''



# agar mein iske ander koi integer value dunga to mera code bilkul sahi se run ho jayega ...... lekin agr mein iske ander kuch aur likh du to mera program crash nahi hoga bss ek error print krega (jab ek bar program crash ho jaye to uske niche ka kuch bhi print nahi hota) lekin yaha bss ek error print hoga kuch crash nahi hoga aur uske niche jo bhi print hona hoga wo print ho jayega
#  this is the syntax of try and exception 
# agar meri chij sahi se try ho gyi to thik hai nahi to wo except k pass chali jayegi aur error print ho jayega (ye bilkul if else statement ki terah hai) try hua to thik hai nahi to except mein chala jayega 
try:
    a = int(input("enter a number "))
    print(a)

except ValueError as v:
    print("heyy")
    print(v)

except Exception as e:
    print(e)

print("thankyou")


# how to raise error
a = int(input("enter a number"))
b = int(input("enter another number"))
if(b==0):
    raise ZeroDivisionError("hey our program is not meant to divide numbers by zero")
else:
    print(f"the division of a/b is {a/b}")


# try with else
# jab try wala code sucessfully run hoga tab mera code else statement mein jayega usko read krega warna nahi
try:
    a = int(input("enter the number "))
    print(a)
 
except Exception as e:
    print(e)

else:
    print("i am inside else")


# try with finally
# finally ka main use ek function k ander hota hai (ek function mein kisi chij ko return kia jata hai to uske aage ka code chalta hi nahi hai) lekin finally mein eisa nahi hota .... function ko return krne k bad bhi finally har haal mein chalega
def main():
    try:
        a = int(input("enter the number "))
        print(a)
        return
    
    except Exception as e:
        print(e)
        return

    finally:
        print("i am inside finally")

main()


# __name__ ko agr mein is file mein run krunga to ye mujhe us file ka nam btayega jaha se meine is function ko import krwaya hai
from module15 import myfunc
# agar mein __name__ ko yaha print krwaunga to mujhe module milega kyuki meine us code ko module wali file mein likha tha



# this code can be simplified by enumerate function
l = [2, 54, 546, 654]
'''index = 0
for item in l:
    print(f"the item number at index {index} is {item}")
    index+=1'''
# let's see
for index, item in enumerate(l):
    print(f"the item number at index {index} is {item}")


# list comprehensive
mylist = [1, 4, 6, 3, 8]
'''squaredlist = []
for item in mylist:
    squaredlist.append(item*item)
print(squaredlist) '''
# this work can be simplified using list comprehensive
squaredlist = [i*i for i in mylist]
print(squaredlist)