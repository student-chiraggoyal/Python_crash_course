# example of a class
class employee:
    position="hr"           # this is a class attribute
    salary=1200000

# class k ander hum is terah se function bhi bna skate hai

    # dunder method which is automatically called
    #jab b koi naya object banega to ye init dunder method apne ap call ho jayega
    def __init__(self, name, salary, position):
        self.name=name
        self.salary=salary
        self.position=position
        print("i am creating an object")

    def getinfo(self):   
        # function k ander ek self dena compulsory hota hai nahi to mera function error dega
        print(f"the position is {self.position} and the salary is {self.salary}")

    @staticmethod           # ye self ko nahi lega iska mtlb hota hai ki isme hume object ka koi attribute nahi chahiye ye bilkul alag se humne isko bnaya hai
    def greet():
        print("good morning everyone")



# here name is object/instance attribute and position and salary are class attributes as they directly belon to the class

# example of an object-----> here chirag is an object
chirag = employee()                 # this is an instance/object attribute
chirag.name = "chirag goyal"
print(chirag.name, chirag.position, chirag.salary)


# another object named rohan
rohan = employee()
rohan.name = "rohan roro robiscon"
rohan.position = "cheif executive officer"    # this is an instance attribute    
  # meine class attribute mein bhi position likha tha aur meine object attribute mein bhi position likha hai lekin preference humesa object attribute ko milegi isiliye wahi position print hogi jo mein object mein likhi hogi
print(rohan.name, rohan.salary, rohan.position)


aman = employee()
aman.position = "excise inspector"
aman.getinfo()      # is terah se class wale function ko use kr skte hai        
     # line 44 aur 46 dono same hai bss dono ko likhne ka tarika alag alag hai
employee.getinfo(aman)
aman.greet()


kanu = employee("kannu", 1400000, "macine learning expert")
# kanu.name = "kaanu sharma"
print(kanu.name, kanu.salary, kanu.position)