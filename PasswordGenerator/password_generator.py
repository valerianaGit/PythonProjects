# DAY 5 
# password generator 
# uses letters(upper and lower cases), symbols and numbers 
# DESIGN
# input how many letters would you like?
# input how many symbols would you like?
# input how many numbers would you like?
# return password 

#====================================================================================First attempt 
import string
import random
letters_lowercase = list(string.ascii_lowercase)
#letters_uppercase = list(string.ascii_uppercase)
#letters_list = [letters_lowercase, letters_uppercase]
symbols_list = list("!@#$%^&*()")
numbers_list = list(range(0,10))
print(letters_lowercase)
#print(letters_uppercase)
print(symbols_list)
print(numbers_list)
print(len(numbers_list)) #length of list
letters_count_str = input("how many letters would you like?")
symbols_count_str = input("how many symbols would you like?")
numbers_count_str = input("how many numbers would you like?") 
def chose_from_list(list_name, times):
    #from a given list_name chose a random item, a set number of times
    random_number = random.randint(0, len(list_name) - 1)
    password_return = []
    for times in list_name:
        password_return.append(list_name[random_number])
        print(password_return)
    return password_return

password_letters = chose_from_list(letters_lowercase, int(letters_count_str))

print(password_letters)
print("Your password is ", password_letters)

