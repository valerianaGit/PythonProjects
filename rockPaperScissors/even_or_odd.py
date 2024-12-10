number_input = int(input("Type any integer your heart desires\n"))
calculation = str(number_input % 2)
print("Calculation = " + calculation)
if number_input % 2 == 0:
    print("That is an even number")
else:
    print("That is an odd number ")