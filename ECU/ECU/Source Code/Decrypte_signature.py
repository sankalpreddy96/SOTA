import rsa

def decrypt_file(file_name, private_key_file):
    with open(file_name, "rb") as input_file:
        encrypted_data = input_file.read()

    with open(private_key_file, "rb") as private_key_obj:
        private_key = rsa.PublicKey.load_pkcs1(private_key_obj.read())

    decrypted_data = rsa.decrypt(encrypted_data, private_key)

    decrypted_file_name = "hashby_signature.txt"  # Change the stored file name
    with open(decrypted_file_name, "wb") as output_file:
        output_file.write(decrypted_data)

    return decrypted_file_name

file_name = "Recive_sending_files\hash_encrypted.txt"
private_key_file = "KEYS\public_key_cloud.pem"

decrypted_file_name = decrypt_file(file_name, private_key_file)

print("The decrypted file has been saved as {}.".format(decrypted_file_name))