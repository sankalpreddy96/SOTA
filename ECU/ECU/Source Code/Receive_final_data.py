import socket

def receive_files(file_names, port):
    # Create a listening socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(('0.0.0.0', port))
        sock.listen(2)  # Listen for 2 simultaneous connections

        print("Waiting for connections...")

        # Accept the incoming connections
        connections = []
        for _ in range(2):
            conn, addr = sock.accept()
            print("Connection established with:", addr)
            connections.append(conn)

        # Receive the files from each connection
        for i, conn in enumerate(connections):
            received_file_name = file_names[i]
            with open(received_file_name, 'wb') as file:
                while True:
                    data = conn.recv(4096)
                    if not data:
                        break
                    file.write(data)

            print("File '{}' has been received from connection {}.".format(received_file_name, i + 1))

    print("All files have been received.")

# File destinations on the receiver
file1_name = 'Received_sending_files\Software_Encrypted.txt'
file2_name = 'Received_sending_files\signature.txt'
file_names = [file1_name, file2_name]

# Port number to listen on
receiver_port = 12358  # Same port number used by the sender

# Receive the files
receive_files(file_names, receiver_port)
