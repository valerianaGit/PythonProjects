greeting = "Welcome to the tip calculator!"
print(greeting)
billTotal = input("What was the total bill?\n")
tipAmount = input("How much tip would you like to give?\n")
numberOfPatrons = input("How many people are splitting the bill?\n")
# formula = (billTotal * 1.tipAmount) / numberOfPatrons 
#tipCalculation = int(tipAmount) / 100
tipTotal = 1 + (int(tipAmount) / 100)
personalBillTotal = (int(billTotal) * tipTotal) / int(numberOfPatrons)  
stringPersonalBillTotal = print("Each person should pay " + "$" + str(personalBillTotal))