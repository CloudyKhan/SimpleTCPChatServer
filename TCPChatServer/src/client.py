# What do we need to create a TCP client? 
# We need to import the sockets module

import socket

# How can we handle receiving messages from the server while sending messages?
# We can use the threading module to handle receiving messages in a separate thread

import threading

# Client Configuration 
# For testing purposes, we will be using our localhost address and the same port number as the server

HOST = '127.0.0.1'
PORT = 12345

# How will the client be able to receive messages from the server? 
# We create a function that runs in a separate thread, which listens for messages from the server

def receive_messages(client_socket):
    while True: 
        try:
            # The recv method receives data from the server, (1024) is the maximum amount of data to be received at once
            message = client_socket.recv(1024).decode('utf-8')
            print(message) 
        except:
            # If an error or disconnection occurs
            print('Disconnected from server') 
            client_socket.close()
            break

# How can we start the client to connect to the server and send/receive messages?
# We create a socket object, connect it to the server, and create threads to handle sending and receiving messages

def main():
    # Create a TCP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    # Connect to the server
    client.connect((HOST, PORT))
    
    # Start a new thread to receive messages from the server
    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()
    
    while True:
        # We read user input and send it to the server - the message is encoded to ensure data integrity
        message = input('') 
        client.send(message.encode('utf-8'))
        
if __name__ == "__main__":
    main()
