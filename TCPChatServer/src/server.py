# This is a walkthrough of my thought process while working on this project.

import socket
import threading

# Server Configuration

HOST = '127.0.0.1'  # Local Host for testing purposes
PORT = 12345  # Non-standard port as a basic security measure and to avoid conflicts

# List to keep track of and store client sockets.
clients = []

# Now we need to be able to handle communications from each client. The way we can do that is by creating a function
# that runs in a separate thread for each client, which listens for messages from the client and broadcasts that to other clients.

def handle_client(client_socket):
    while True:
        try:
            # How can we receive messages from the client?
            # There is a recv method in the socket object to receive data.
            # The recv method receives data from the client socket. The argument (1024) specifies the max amount of data to be received at once (in bytes).
            message = client_socket.recv(1024).decode('utf-8')
            
            # Now that we have received the message from the client, we will need to send the message to other clients.
            # We can create a broadcast function that sends the message to all connected clients except the sender.
            broadcast(message, client_socket)
        except:
            # What if an error occurs or the client disconnects?
            # We can remove the client from the clients list and close the socket.
            clients.remove(client_socket)
            client_socket.close()
            break

# How do we broadcast the messages we received to all of our clients?
# We will need to iterate over the client list and send the message to each of the clients in that list.

def broadcast(message, client_socket):
    # So, how do we iterate over each client in the client list? We can create a for loop to iterate over each client.
    for client in clients:
        # We need to make sure that the client is not the sender to avoid echoing the message back to the sender.
        if client != client_socket:
            try:
                # Now we will send the message data to the client socket. The message is encoded before being sent.
                client.send(message.encode('utf-8'))
                # Why do messages need to be encoded before being sent? There are several important reasons.
                # Network protocols such as TCP/IP transmit data as binary (byte) streams. Any data being sent over the network must be in binary format.
                # Encoding a string message into bytes ensures that it can be transmitted over the network.
                # Encoding also ensures that the characters in the message are represented in a consistent format, such as UTF-8, which is essential for
                # interoperability (ensures different systems and apps can properly interpret the data) and standardization (UTF-8 is a widely used encoding
                # standard that supports a vast range of characters from different languages).
                # Encoding helps maintain the integrity of the data during data transmission, and ensures an accurate reconstruction of the message at the receiving
                # end through decoding back into a string. This process maintains the integrity of the message by ensuring the message remains unchanged.
            except:
                # If sending fails (e.g., the client disconnected), we close the client's socket and remove the client from the clients list.
                client.close()
                clients.remove(client)

# Main function to start the server
# How can we actually start the server to listen for connections?
# We can create a socket object, bind it to the host and port, and call listen to start listening for connections.

def main():
    # The socket function creates a new socket. AF_INET specifies IPv4, and SOCK_STREAM specifies a TCP socket.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # How can we bind the socket to a specific host and port? We can use server.bind.
    server.bind((HOST, PORT))
    
    # Now we need to enable the server to accept connections. The way we do that is by using the .listen method. The argument (5) specifies the maximum number of queued connections.
    server.listen(5)
    print(f'Server started on {HOST}:{PORT}')
    
    # How can we enable the server to accept incoming client connections continuously? With the current configuration, the server would stop accepting connections after the first connection.
    # We can use a while loop to continuously accept new client connections. This loop runs indefinitely, allowing the server to accept new client connections continuously.
    
    while True:
        # The accept method waits for an incoming connection, and returns a new socket representing the connection, and the address of the client.
        client_socket, addr = server.accept()
        print(f'New connection from {addr}')
        
        # We add the new client socket to the clients list.
        clients.append(client_socket)
        
        # We will also create a new thread to handle communication with the new client - allowing the server to handle multiple clients simultaneously.
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()
        
if __name__ == "__main__":
    main()
