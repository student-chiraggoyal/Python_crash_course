# The program will accept two numerical inputs from the user.It will then accept an operator (+, -, *, /) from the user to perform the respective arithmetic operation.The program should handle cases such as invalid input (non-numeric input), division by zero, and invalid operators.If the input is correct, it will return the result of the arithmetic operation.

'''def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("invalid input")

def get_operator():
    valid_operators = ['+', '-', '*', '/']
    while True:
        operator = input("enter the opeartor (+, -, *, /): ")
        if operator in valid_operators:
            return operator
        else:
            print("the operator is invalid")

def perform_operation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2
    if operator == '/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "error : divide by zero is not allowed"

def main():
    num1 = get_number("enter the number-1 : ")
    num2 = get_number("enter the number-2 : ")
    operator = get_operator()
    result = perform_operation(num1, num2, operator)
    print(f"the result of {num1} {operator} {num2} is {result}")
main()'''


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("please enter the valid number")

def get_operator():
    opeartors = ['+', '-', '*', '/']
    while True:
            operator = input("enter the operator from {+, -. *. /}: ")
            if operator in opeartors:
                return operator
            else:
                print("invalid operator")

def perform_operation(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == "/":
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "division by zero is not allowed"

def calculator():
    num1 = get_number("enter the value of number 1: ")
    num2 = get_number("enter the value of number 2: ")
    operator = get_operator()
    result = perform_operation(num1, num2, operator)
    print(f"the result of {num1} {operator} {num2} is {result}")
calculator()