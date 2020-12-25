from sympy.crypto.crypto import encipher_hill,decipher_hill
from sympy import Matrix

key=Matrix([[1,2],[3,5]])
choose=int(input("Enter 1 to decode or 0 to encode "))
if choose==1:
    sentence=input("Enter the cipher tect to be decoded ")
    print("The output is without space ",decipher_hill(sentence, key))
else:
    sentence=input("Enter text to encoded ")
    print(encipher_hill(sentence, key))