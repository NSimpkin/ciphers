# Declare a string variable and name it plainText
# Declare another two string variables and name them leftPT, rightPT, and assign to them empty strings; e.g. leftPT = "";
# Assign to plainText user input
# Use a for loop to concatenate to leftPT all of the letters from plainText that are in even indexes, and all of the letters from odd indexes to rightPT.
# 4 % 2 == 0    This means that 4 is an even number
# Output the two variables after the for loop ends to create a railway cipher.
# E.g. if the input is meetatdawn the output will be meadwettan

plainText = input("Please enter the plaintext: ")
leftPT = ""
rightPT = ""

for index in range (0, len(plainText)):
    if index%2==0:
        leftPT+=plainText[index]
    else:
        rightPT+=plainText[index]
print (leftPT+rightPT)