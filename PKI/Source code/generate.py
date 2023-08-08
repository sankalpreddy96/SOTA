import rsa
import os
key = rsa.newkeys(2048)
private_key = key[1]
public_key = key[0]
os.chdir("KEYS/")
l=['car','cloud']
for i in l:
    with open('private_key_'+i+'.pem', 'wb') as f:
        f.write(private_key.save_pkcs1())
    
    with open('public_key_'+i+'.pem', 'wb') as f:
        f.write(public_key.save_pkcs1())
