'''
  *
 ***
*****
'''
# num=int(input("enter the number "))
# for i in range(1,num+1):
#     print(" "*(num-i),end="")
#     print("*"*(2*i-1),end="")
#     print("")

'''
*****
 ***
  *
'''
# num=int(input("enter the number "))
# for i in range(1,num+1):
#     print(" "*((num-1)-(num-i)),end="")
#     print("*"*(2*num-(2*i-1)),end="")
#     print("")

'''
    *
   * *
  * * *
 * * * *
* * * * *
'''
# num=int(input("enter the value "))
# for i in range(1,num+1):
#     print(" "*(num-i),end="")
#     print("* "*i,end="")
#     print("")

'''
* * * * *
 * * * *
  * * *
   * *
    *
'''
# num=int(input("enter the value "))
# for i in range(1,num+1):
#     print(" "*((num-1)-(num-i)),end="")
#     print("* "*((num+1)-i),end="")
#     print("")

'''
      A 
     A B 
    A B C 
   A B C D 
  A B C D E 
'''

num=int(input("enter the value "))
var=65
for i in range(1,num+1):
    print(" "*(num-i),end="")
    print(chr(var),end="")
    var+=1
    print("")