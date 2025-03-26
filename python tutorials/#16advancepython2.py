# this all work can be replaced by using lambda function
def square(n):
    return (n*n)
print(square(5))

# in this way
square = lambda x: x*x
print(square(7))

add = lambda a,b,c : a+b+c
print(add(3,4,5))


# join method
a = ["chirag", "rohan", "shbahm"]
final = "-".join(a)
print(final)


# format method
a = "{0} is a good {1}".format("chirag", "boy")       # by default jo empty brackets hai unki value 0 aur 1 hoti hai agar mein ye dono arguments change karna chhata hu to mein inki value ko interchange kr dunga
print(a)

b = "{1} is a good {0}".format("chirag", "boy")
print(b)


# map function
l = [1, 3, 5, 7, 8]
squaree = lambda x: x*x
sqrlist = map(squaree, l)
print(list(sqrlist))


# filter function
l1 = [1, 2, 3, 4, 5, 6, 7, 8]
def even(n):
    if(n%2==0):
        return True
    return False

onlyeven = filter(even, l1)
print(list(onlyeven))


# reduce function
from functools import reduce
l2 = [3, 4, 5, 6]
def sum(a, b):
    return a+b
mul = lambda x,y : x*y
print(reduce(sum, l2))
print(reduce(mul, l2))