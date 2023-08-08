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

# File to be sent
file_name = 'Tester\Recive_sending_files\ECU_public_key_request.txt'

# Receiver's address and port
receiver_host = '192.168.170.119'  # Replace with the actual receiver's IP address
receiver_port = 12358  # Replace with the actual receiver's port number

# Send the file
send_file(file_name, receiver_host, receiver_port)