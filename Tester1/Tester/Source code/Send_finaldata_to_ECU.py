import socket

def send_file(file_name, host, port):
    with open(file_name, 'rb') as file:
        file_data = file.read()

    # Connect to the receiver
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))

        # Send the file data
        sock.sendall(file_data)

    print("File '{}' has been sent to {}:{}.".format(file_name, host, port))

# Files to be sent
file1_name = 'Tester\Recive_sending_files\Software_Encrypted.txt'
file2_name = 'Tester\Recive_sending_files\signature.txt'

# Receiver's address and port
receiver_host = "192.168.170.193"
receiver_port = 12358  # Same port number used by the receiver

# Send the files
send_file(file1_name, receiver_host, receiver_port)
send_file(file2_name, receiver_host, receiver_port)
