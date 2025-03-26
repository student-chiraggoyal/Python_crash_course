def myfunc():
    print("hello world")


if __name__ == "__main__":
    print("we are directly running this code")
    myfunc()
    print(__name__)     # agr mein __ name__ ko isi file mein run kruga to yaha pe mujhe __main__ print kr dega 


# agar mein is code ko isi file mein execute krunga to ye sab print ho jayega lekin agar isko kisi aur file mein import krke run krne ki kosish krunga to nahi hoga


a = 89      # global variable isko mein kisi bhi function mein use kr skta hu
def fun():
    global a        #is global keyword ki help se mein a=89 ki value change krke a=3 kr di isiliye dono bar a ki value 3 print ho rahi hai
    a = 3
    print(a)
fun()
print(a)