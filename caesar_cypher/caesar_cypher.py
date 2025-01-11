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
        
