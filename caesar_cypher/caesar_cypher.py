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

        
#========================================= ENCODE ========================================
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
#========================================= ENCODE ========================================

# TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        output_text += letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")



# TODO-3: Can you figure out a way to restart the cipher program?
    repeat = input("Would you like to go again? Type 'yes' or 'no'")
    if repeat == "yes":
        direction_again = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text_again = input("Type your message:\n").lower()
        shift_again = int(input("Type the shift number:\n"))
        caesar(original_text=text_again, shift_amount= shift_again,encode_or_decode= direction_again)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
