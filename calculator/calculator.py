# Functions with outputs -> CALCULATOR APP
#=======================================================================
# 2 number inputs, 4 operations 
first_number = int(input("What's the first number?\n"))
operation_chosen = input("\n+\n-\n*\n/\nPick an operation\n")
second_number = int(input("What's the second number?\n"))
#total = 0
#=======================================================================
def calculator_brain(first_number, second_number, operation_chosen):
    if operation_chosen == "+":
        print(" operation chosen", "+")
        total = first_number + second_number
    elif operation_chosen == "-":
        print(" operation chosen", "-")
        total = first_number - second_number
    elif operation_chosen == "*":
        print(" operation chosen", "*") 
        total = first_number * second_number
    elif operation_chosen == "/":
        print(" operation chosen", "/") 
        total = first_number / second_number 
    print(total)
    return total
calculator_brain(first_number, second_number, operation_chosen)