from caesarcipher import CaesarCipher
#cipher=CaesarCipher('B ptgm mh xgvhwx mabl lmkbgz')
#print(cipher.cracked)
choose=int(input("Enter 1 to decode or 0 to encode "))
if choose==1:
    sentence=input("Enter the cipher tect to be decoded ")
    print(CaesarCipher(sentence).cracked)
else:
    sentence=input("Enter text to encoded ")
    print(CaesarCipher(sentence).encoded)