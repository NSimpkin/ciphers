# WATCH PART 1 - https://www.youtube.com/watch?v=4zahvcJ9glg
# WATCH PART 2 - https://www.youtube.com/watch?v=oOcTVTpUsPQ

p=input("Please enter a prime number p: ")
p_is_prime=False
while p_is_prime==False:
    for i in range(2,p):
        if (p%i) == 0:
            print ("p must be a prime number, please try again")
        else:
            p_is_prime=True
q=input("Please enter a prime number q: ")
q_is_prime=False
while q_is_prime==False:
    for i in range(2,q):
        if (q%i) == 0:
            print ("q must be a prime number, please try again")
        else:
            q_is_prime=True
if p_is_prime==True and q_is_prime==True:
    N=p*q
    coprimes = (p - 1)*(q - 1)
    print("Possible encryption keys:")
    for x in range(2, coprimes):
        for i in range(2, x):
            if (x%i)!=0:
                if (N%x)!=0:
                    print (x)
    e=input("Choose your encryption key, c, from the list above: ")
    print("Possible decryption keys:")
    for y in range(0, ((coprimes*coprimes)/(coprimes/2))):
        if (y*e)%N==1:
            print(y)
    d=input("Choose your decryption key, d, from the list above: ")
    print("Your encryption keys are: " + str(e) + ", " + str(N))
    print("Your decryption keys are: " + str(d) + ", " + str(N))
    print("To encrypt a character, follow the formula: (asc(char)^" + str(e) + ")MOD" + str(N))
    print("To decrypt a character, simply follow the formula: (asc(char)^" + str(d) + ")MOD" + str(N)) 

# Step[1]
# User inputs two primary numbers 
# STRETCH - validate that the input is in fact a prime number

# Step[2]
# Multiply the two prime numbers and store in a variable. This will be the modulus in the encyption and decryption keys

# Step[3]
# Find the amount of Co-Prime numbers with the number in Step[2]

# Step[4] - Encryption 
# Output the numbers which are between 1 and the number in Step[3], not inclusive, and are Co-Prime with number in Step[2] and Step[3]
# Allow user to input the number they wish to choose from the list

# Step[5] - Decryption
# Output the numbers which are 1 when a number is multiplied with Encryption number, modulus Step[3] number
# Allow user to input the number they wish to choose from the list

# Step[6]
# Output to the encryption and decryption keys together with their modulus
# The format should be 
# ( ord(char)^encryptionKey ) MOD Step[2]
# ( ord(char)^decryptionKey ) MOD Step[2]
