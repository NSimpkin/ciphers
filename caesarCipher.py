# Why is plainText a string and shiftAMount an integer?
# plainText is used as text, shiftAmount is used as a number

# Why is cipherText declared as an empty string?
# it will be generated as the code runs

# How many times does the for loop iterate?
# as many times as there are characters in the plainText

# Describe the function of this line cipherText += chr(ord(plainText[c]) + shiftAmount)
# adds to the cipherText the unicode value of the letter at that point in the Plaintext plus the shift by the chosen number

def caesar_encrypt():
    plainText = input("Please enter the plaintext: ").upper()
    shiftAmount = int(input("Please enter the shift amount: "))
    cipherText = ""

    for c in range(0, len(plainText)):
        cipherText += chr(ord(plainText[c]) + shiftAmount)
        
    print (cipherText)

def caesar_decrypt():
    cipherText = input("Please enter the ciphertext: ").upper()
    shiftAmount = int(input("Please enter the shift amount: "))
    plainText = ""

    for c in range(0, len(cipherText)):
        plainText += chr(ord(cipherText[c]) - shiftAmount)
        
    print (plainText)

menu = True
while menu:
    print ("Caesar Cipher Options")
    print ("1) ENCRYPT")
    print ("2) DECRYPT")
    print ("3) Quit")
    menuChoice = int(input("Please make your choice: "))
    if menuChoice == 1:
        menu = False
        caesar_encrypt()
    elif menuChoice == 2:
        menu = False
        caesar_decrypt()
    elif menuChoice == 3:
        menu = False
    else:
        print("You did not select from the options, please try again")

# MAIN TASK - Add to this program a method to also decrypt
# Add a menu system from which the user can choose which action they wish to take
# The program should keep requesting the user to choose from the menu until 
# they have made the correct choice: 1) Encrypt     2) Decrypt      3) Quit

# STRETCH - Modify the code so that if one of the letters in the plainText is Z
# and the shiftAmount is 3, then that character will shift to C instead of ]