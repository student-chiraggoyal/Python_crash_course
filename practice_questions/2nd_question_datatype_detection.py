# Create a Python program that takes three inputs from the user and determines the data type of each input. It should identify whether the input is an integer, float, or string.


'''def data_type(value):
    try:
        int_value = int(value)
        print(f"the datatype of the {value} is: integer")
    except ValueError:
        try:
            float_value = float(value)
            print(f"the datatype of the {value} is: float")
        except ValueError:
            print(f"the datatype of the {value} is: string")

def main():
    input1 = input("enter the value-1: ")
    input2 = input("enter the value-2: ")
    input3 = input("enter the value-3: ")
    data_type(input1)
    data_type(input2)
    data_type(input3)
main()
'''



def data_type(value):
    try:
        int_value = int(value)
        print(f"the datatype of the {value} is: integer")
    except ValueError:
        try:
            float_value = float(value)
            print(f"the datatype of the {value} is: float")
        except ValueError:
            print(f"the datatype of the {value} is: string")


def main():
    input1 = input("enter the input1; ")
    input2 = input("enter the input2; ")
    input3 = input("enter the input3; ")
    data_type(input1)
    data_type(input2)
    data_type(input3)
main()