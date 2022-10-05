import optparse

# Takes in a plaintext message
# and an integer key and encrypts
# using the Caesar cipher approach
def encrypt(msg, key):

    # Our encrypted array of characters
    result = []
    # Our full cipher text
    message = ""

    # Take every character and get is ASCII form
    # Then slide every number down/up using the key
    for char in msg:
        
        # Spaces are added to the string with no encryption
        if (char == ' '):
            result.append(" ")
            
        # Uppercase letters converted to ASCII, then MOD enforces the wrap around rules 
        elif (char.isupper()):
            result += chr((ord(char) + key-65) % 26 + 65)
            
        # Same process for lowercase letters                                 
        else:
            result += chr((ord(char) + key-97) % 26 + 97)

            
    # Gather characters into cipher text and print
    for i in result:
        if ( i == " "):
            message += i
        else:
            message += i           
    print(message)
               

# Takes in an encrypted message
# and an integer key and decrypts
# using the Caesar cipher approach
def decrypt(msg, key):

    # Our encrypted array of characters
    result = []
    # Our full cipher text
    message = ""

    for char in msg:
        
        # Spaces are added to the string with no encryption
        if (char == ' '):
            result.append(" ")
            
        # Uppercase letters converted to ASCII, then MOD enforces the wrap around rules 
        elif (char.isupper()):
            result += chr((ord(char) - key-65) % 26 + 65)
            
        # Same process for lowercase letters                                 
        else:
            result += chr((ord(char) - key-97) % 26 + 97)

    # Gather characters into cipher text and print
    for i in result:
        if ( i == " "):
            message += i
        else:
            message += i           
    print(message)
        



def main():
    parser = optparse.OptionParser("usage%prog "+ "-f <decrypt | encrypt> -m <message> -k <key>")
    parser.add_option('-f', dest='function', type='string', help='[ decrypt | encrypt ]')
    parser.add_option('-m', dest='msg', type='string',  help='message to encrypt (plaintext) or decrypt (encrypted)')
    parser.add_option('-k', dest='key', type='int', help='cipher key as an integer')
    (options, args) = parser.parse_args()
    function = options.function
    if ((function != "encrypt" and function != "decrypt") or function == None):
        print('[-] You must specify a valid function: "encrypt" or "decrypt"')
        exit(0)
    msg = str(options.msg)
    key = int(options.key)
    if (msg == None) | (key == None):
        print('[-] You must specify a message and key.')
        exit(0)
    if function == "encrypt":
        encrypt(msg, key)
    elif function == "decrypt":
        decrypt(msg, key)

if __name__ == '__main__':
    main()

