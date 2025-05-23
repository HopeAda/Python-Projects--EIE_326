alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cipherMessage():
    messageToCipher = str(input("What is the message you want to cipher? \n"))
    shiftNumber = int(input("By how much are you shifting the message? \n"))
    
    shiftedMessage = ""

    for letter in messageToCipher:
        if letter not in alphabets:
            shiftedMessage += letter
        
        else:
            newIndex = alphabets.index(letter.lower())+shiftNumber
            if newIndex > (len(alphabets) - alphabets.index(letter.lower())):
                    
                newIndex = newIndex % len(alphabets)
            if letter == letter.upper():
                shiftedMessage += alphabets[newIndex].upper()
            else:
                shiftedMessage += alphabets[newIndex]
            

    print("Your ciphered message is", shiftedMessage);
    
    

def decipherMessage():
    messageToDecipher = str(input("What is the message you want to decipher? \n"))
    shiftNumber = int(input("What are you shifting it back by? "))
    
    unshiftedMessage = ""
    for letter in messageToDecipher:
        if letter not in alphabets:
            unshiftedMessage += letter
        else:
            newIndex = alphabets.index(letter.lower()) - shiftNumber
            if shiftNumber > len(alphabets):
                newIndex = newIndex % len(alphabets)

            if letter == letter.upper():
                unshiftedMessage += alphabets[newIndex].upper()
            else:
                unshiftedMessage += alphabets[newIndex]
        
    print("Your deciphered message is", unshiftedMessage)
    
        


def main():
    print("This is a caesar cipher")
    print("Do you want to create a cipher of a message, or decipher one?")
    letter = input("Type A for Cipher and B for Decipher \n")
    
    if letter.upper() == 'A':
        cipherMessage()
    
    if letter.upper() == 'B':
        decipherMessage()

main()


