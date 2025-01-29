# Functions with outputs -> CALCULATOR APP
#=======================================================================
# 2 number inputs, 4 operations 
first_number = input("What's the first number?\n")
operation_chosen = input("\n+\n-\n*\n/\nPick an operation\n")
second_number = input("What's the second number?\n")
#=======================================================================
def calculator_brain(first_number, second_number, operation_chosen):
    total = 0
    int_one = int(first_number)
    int_two = int(second_number)
    if type(int_one) != int:
        print("please chose an integer for your first number, start again")
        return
    if type(int_two) != int:
        print("please chose an integer for your second number, start again")
        return
    if operation_chosen == "+":
        print(" operation chosen", "+")
        total = int_one + int_two
    elif operation_chosen == "-":
        print(" operation chosen", "-")
        total = int_one - int_two
    elif operation_chosen == "*":
        print(" operation chosen", "*") 
        total = int_one * int_two
    elif operation_chosen == "/":
        print(" operation chosen", "/") 
        total = int_one / int_two
    #print(total)
    return total
total = calculator_brain(first_number, second_number, operation_chosen)
print("The total is ",total)