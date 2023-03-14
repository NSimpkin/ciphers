# What is the function of the first for loop which appends to cipherKey?
# adds the converted letters using their unicode values

# What is the if statement (SELECTION) checking for, and what action does it take if it is true?
# if a letter in the plaintext matches one in the alpha array, and if so it adds the corresponding letter from the cipherKey array to cipherText

# Why is a nested loop being used in the second for loop?
# to cycle through each letter in the plaintext and each letter of the alphabet for that letter

def atbash_cipher():
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    cipherKey = []
    plainText = input('Please enter the plaintext: ').upper()
    cipherText = ""
    for k in range(90, 64, -1):
        cipherKey.append(chr(k))
    for i in range(0, len(plainText)):
        for x in range(0, 26):
            if plainText[i] == alpha[x]:
                cipherText += cipherKey[x]              
    print ("Using the atBash cipher, this is the cipher-text: " + cipherText)

def keyword_cipher():
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    cipherKey = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    plainText = input('Please enter the plaintext: ').upper()
    keyWord = input('Please enter the keyword: ').upper()
    cipherText = ""

    keyWord = keyWord[::-1]
    for char in keyWord:
        if char in alpha:
            cipherKey.pop(cipherKey.index(char))
        if char not in cipherKey:
            cipherKey.insert(0, char)
    # print (cipherKey)
    for i in range(0, len(plainText)):
        for x in range(0, 26):
            if plainText[i] == alpha[x]:
                cipherText += cipherKey[x] 
    print ("Using the keyword cipher, this is the cipher-text: " + cipherText)

menu = True
while menu:
    print ("Options")
    print ("1) ATBASH CIPHER")
    print ("2) KEYWORD SHIFT CIPHER")
    print ("3) Quit")
    menuChoice = int(input("Please make your choice: "))
    if menuChoice == 1:
        menu = False
        atbash_cipher()
    elif menuChoice == 2:
        menu = False
        keyword_cipher()
    elif menuChoice == 3:
        menu = False
    else:
        print("You did not select from the options, please try again")

# MAIN TASK - Add a menu system to this program, and allow the user to choose from two types of ciphers
# atBash and Keyword. Add to the program the algorithm which will encrypt a plainText using the Keyword
# cipher and output that to the user

# STRETCH - Don't forget to stretch, sitting in front of a computer all day is not healthy. 
# Your muscles need movement