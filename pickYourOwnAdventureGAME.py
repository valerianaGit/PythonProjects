# Conditional statements, logical operators, code blocks and scope => if else statements,
#if condition:
#    do this
#    else
#    do this 
start = input("Choose left or right \n")
left = "left"
right = "right"
gameOver = "You died. Game Over"
if start == left:
    firstLevel = input("You find 3 boxes, Choose which to open between pandora, puppies, void\n")
    if firstLevel == "pandora":
        print("You have unleashed the full wrath of the gods " + gameOver)
    elif firstLevel == "puppies":
        print("You win at life forever and live happily every after! And you get to have a puppy! ")
    else:
        print("That was a weird choice but, ok " + gameOver)
else:
    print(gameOver)

