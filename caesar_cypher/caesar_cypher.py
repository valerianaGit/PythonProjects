#Encryption program , each letter is shifted by a pre determined amount 
#type the message and the shift number , 
# return the encoded result
# then to decode the person must type decode, 
# enter the message and the shift number and the cypher will;
#  return the deciphered message 
#===============================================
# DESIGN 
# ENCODE OR DECODE 
# IF ENCODE  ask for message to encode AND shift number => 
# LOOK AT ALPHABET, for every letter in our message, 
# take each letter and shift its space in the alphabet by the shift number 
# = find this letter and append (join) it to a string , return the string 
# IF DECODE  ask for message to DEcode AND shift number 
#===============================================
import string
#alphabet = string.ascii_lowercase
input_message = input("Input your message \n").strip().lower()
shift_number = int(input("Input your shift number \n"))

#hello, shift 1 => elloh
def encode(message, shift):
    return_message = ""
    for i, char in enumerate(message):
        new_char = message[i + shift]
        print(new_char)
        "".join(new_char)
       # print(return_message)
    print("Your encoded message is ", "".join([return_message, new_char]))
    return return_message
encode(input_message, shift_number)

#def encode2(message, shift):
 #   for i, char in message:
  #      new_char = message[i + shift]
        
#========================================= ENCODE
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabets = alphabet + alphabet + alphabet + alphabet

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):
    encrypted_message = ""
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
    for letter in original_text:
        index = alphabet.index(letter)
        new_letter = alphabets[index + shift_amount]
        #print(new_letter)
        encrypted_message += new_letter
    print(f"The encrypted message is {encrypted_message}")
    return encrypted_message
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
encrypt("z",9)
# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
encrypt(text, shift)
