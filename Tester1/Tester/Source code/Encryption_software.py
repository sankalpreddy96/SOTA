import rsa

def encrypt_file(file_name, public_key_file):
    with open(file_name, "rb") as input_file:
        data = input_file.read()

    with open(public_key_file, "rb") as public_key_file:
        public_key = rsa.PublicKey.load_pkcs1(public_key_file.read())

    encrypted_data = rsa.encrypt(data, public_key)

    encrypted_file_name = "Tester\Recive_sending_files\Software_Encrypted.txt"
    with open(encrypted_file_name, "wb") as output_file:
        output_file.write(encrypted_data)

    return encrypted_file_name


file_name = "Tester\Recive_sending_files\Software.txt"
public_key_file = "Tester\KEYS\public_key_car.pem"

encrypted_file_name = encrypt_file(file_name, public_key_file)

print("The encrypted file has been saved as {}.".format(encrypted_file_name))