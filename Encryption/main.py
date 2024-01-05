import rsa

public_key, private_key = rsa.newkeys(1024)

#print(private_key)

with open("public.pem", "rb") as f:
    #f.write(public_key.save_pkcs1("PEM"))
    #f.write("Hey")
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("private.pem", "rb") as f:
    #f.write(private_key.save_pkcs1("PEM"))
    #f.write("Whazup")
    public_key = rsa.PrivateKey.load_pkcs1(f.read())


#message = "Hello everybody"

#encrypted_message = rsa.encrypt(message.encode(), public_key)
#print(encrypted_message)
encrypted_message = open("encrypted.message", "rb").read()

clear_message = rsa.decrypt(encrypted_message, private_key)
print(clear_message.decode())