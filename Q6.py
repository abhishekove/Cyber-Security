from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad

key = b'Sixteen byte key'
iv = b'\xe8\\R0\xf0\xfe\xd8J'
cipher = DES3.new(key, DES3.MODE_CBC, iv)
choose=int(input("Enter 1 to decode or 0 to encode "))
if choose==1:
    #Encode the text and paste it below to check
    plaintext=b'\x13e\xb6\xb2\xf0$\x9c\xcco\xc5Hm\x90\x08@\x11\xect\x9b\x1d\xc7\x08\xad\x97\xe6Un\x873\xbb\x9e\xe2\xb0*\xa1^\xbb\xd7f\x1b\x03\xf4R\xa5T\xb3ku'
    print(str(cipher.decrypt(pad(plaintext,DES3.block_size))).split("\\")[0][2:])
else:
    plaintext=input("Enter text to encoded ")
    print(cipher.encrypt(pad(plaintext.encode('UTF-8'),DES3.block_size)))