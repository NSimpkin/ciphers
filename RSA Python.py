#Does not work with all keys that are generated
#The two prime numbers 13 and 17 are tested to work
#From the numbers they generate 101 as the encryption key
#and 173 as the decryption key have been tested with
#the value 65 (A in ASCII) to work
#13    17    101    173
p1 = int(input("Enter first prime number: "))
p2 = int(input("Enter second prime number: "))
N = p1 * p2

print ("The result of multiplying prime 1 and prime 2 is " + str(N))

#numbers between 1 and value of N that share common factors with N
coPrimes = (p1 - 1)*(p2 - 1)
#coprime mean they share no common factor with N
print ("Total numbers that are coprime with " + str(N) + " are " + str(coPrimes))

print ("Possible Encyption Keys from those coprimes: ")
for i in range(2,coPrimes + 1):
  if str(coPrimes / i)[:-1] != '0' and str(N / i)[:-1] != '0':
    if not (coPrimes % 2 == 0 and i % 2 == 0 and coPrimes % 2):
      for y in range(1, coPrimes + 1):
        if (i * y) % coPrimes == 1:
          print (i)
  
encryptionKey = int(input("Please choose your encryption key: "))

#Reduce the amount of decryption key
if coPrimes < 50: dCounter = 100
if coPrimes > 51 and coPrimes < 100: dCounter = 500
if coPrimes > 101 and coPrimes < 400: dCounter = 1000
if coPrimes > 401: dCounter = 10000


print ("")
print ("Possible Decryption Keys from those coprimes: ")  
for i in range(1, dCounter + 1):
  if encryptionKey * i % coPrimes == 1 and i != encryptionKey:
    print (i)

decryptionKey = int(input("Please choose your decryption key: "))

print("")
print("Your encryption keys are: " + str(encryptionKey) + ", " + str(N))
print("Your decryption keys are: " + str(decryptionKey) + ", " + str(N))

print("")
print("")
print("To encrypt a character, simply follow the formula: (asc(char)^" + str(encryptionKey) + ")MOD" + str(N))
print("To decrypt a character, simply follow the formula: (asc(char)^" + str(decryptionKey) + ")MOD" + str(N))       




