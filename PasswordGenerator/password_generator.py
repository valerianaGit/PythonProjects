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
letters_count_str = input("how many letters would you like?\n")
symbols_count_str = input("how many symbols would you like?\n")
numbers_count_str = input("how many numbers would you like?\n") 
def chose_from_list(list_name, times):
    #from a given list_name chose a random item, a set number of times
    password_return = []
    for item in list_name:
        random_number = random.randint(0, len(list_name) - 1)
        password_return.append(list_name[random_number])
        print(password_return)
    return password_return

password_letters = chose_from_list(letters_lowercase, int(letters_count_str))

print(password_letters)
print(len(password_letters))
print("Your password is ", password_letters)

#================OPTION 2 REVISED================================================================
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
new_password = ""
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
def random_number_generator_for(list):
    length = len(list)
    return random.randrange(0,length)
letters_random_number = random_number_generator_for(letters)
def find_password_items_from_list(list, items, password):
    for i in range(items):
        choice = random.choice(list)
        password += choice
    print(password)
    return password
letters_password = find_password_items_from_list(letters, nr_letters, new_password)
symbols_password = find_password_items_from_list(symbols, nr_symbols, new_password)
numbers_password = find_password_items_from_list(numbers, nr_numbers, new_password)
final_password = letters_password + symbols_password + numbers_password
print(final_password)

def randomize_password(password):
    char_list = list(password)
    random.shuffle(char_list)
    randomized_string = "".join(char_list)
    return randomized_string
random_password = randomize_password(final_password)
print(random_password)