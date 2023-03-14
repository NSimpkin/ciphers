# Declare a string variable and name it plainText
# Assign to plainText user input
# If the user input is less than 6 letters, the program should output: "Not enough letters"
# How the cipher works:
# If the input is 
# WEAREDISCOVEREDFLEEATONCE 
# then the algorithm will sort it into columns
# The columns will look like this
# W E A R E D
# I S C O V E 
# R E D F L E 
# E A T O N C 
# E  
# Once they have been organised in this manner then the algorithm will choose the columns at random (Variables) in the following order
# 6 4 2 1 3 5
# W E A R E D
# I S C O V E 
# R E D F L E 
# E A T O N C 
# E  
# Then the algorithm will output the following data ROFO ACDT EVLN ESEA WIREE

def columnar_encrypt():
    columns= ["", "", "", "", "", ""]
    for char in range(0, len(plainText)):
        for i in range(0, 6):
            if columns[i]==min(columns, key=len):
                columns[i]=columns[i]+plainText[char]
                break
        char+=1
    ciphertext=columns[3]+" "+columns[2]+" "+columns[4]+" "+columns[1]+" "+columns[5]+" "+columns[0]
    print(ciphertext)

tooshort=True
while tooshort:
    plainText=input("Please enter the plaintext, without spaces: ")
    if len(plainText)>=6:
        tooshort = False
        columnar_encrypt()
    else:
        print("Not enough letters, please try again with 6 or more")

