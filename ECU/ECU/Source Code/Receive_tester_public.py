import socket
def receive_file(file_name, port):
    # Create a listening socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(('0.0.0.0', port))
        sock.listen(1)

        print("Waiting for a connection...")

        # Accept the incoming connection
        conn, addr = sock.accept()
        print("Connection established with:", addr)

        # Receive the file data
        with open(file_name, 'wb') as file:
            while True:
                data = conn.recv(4096)
                if not data:
                    break
                file.write(data)

    print("File '{}' has been received.".format(file_name))

# File destination on the receiver
file_name = 'C:\Users\91798\Desktop\SOTA\ECU\ECU\KEYS\public_key_cloud.pem'

# Port number to listen on
receiver_port = 12358  # Same port number used by the sender

# Receive the file
receive_file(file_name, receiver_port)
