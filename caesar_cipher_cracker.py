
def cracker():

    msg = "Yrzc Trvjri"

    # Our decrypted array of characters
    result = []
    # Our full plaintext
    message = ""
    for i in range(26):
        for char in msg:
        
            # Spaces are added to the string with no decryption
            if (char == ' '):
                result.append(" ")
            
            # Uppercase letters converted to ASCII, then MOD enforces the wrap around rules 
            elif (char.isupper()):
                result += chr((ord(char) - i-65) % 26 + 65)
            
            # Same process for lowercase letters                                 
            else:
                result += chr((ord(char) - i-97) % 26 + 97)
        result += '\n'

    # Gather characters into full plaintext and print
    for i in result:
        if ( i == " "):
            message += i
        else:
            message += i
    print(message)


def main():
    main()
    
