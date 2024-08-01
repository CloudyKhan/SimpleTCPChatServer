# TCP Chat Server

This project demonstrates a simple TCP chat server and client implementation in Python. The server can handle multiple client connections simultaneously and broadcast messages from one client to all other connected clients.

### Prerequisites

- Python 3.x

### Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/dkhan25/SimpleTCPChatServer.git
   cd SimpleTCPChatServer/TCPChatServer
   ```

2. **Navigate to the Source Directory**:
   ```sh
   cd src
   ```

### Running the Server

1. **Run the server**:
   ```sh
   python3 server.py
   ```

### Running the Client

1. **Run the client**:
   ```sh
   python3 client.py
   ```
   
### Connecting Multiple Clients

Up to 5 clients can be connected simultaneously, each on a different terminal. If you need to adjust the maximum number of clients, modify the server.listen(5) line in server.py where the argument 5 specifies the maximum number of queued connections.

**Note**: The current configuration is suitable for testing purposes but is **not** secure for a live environment. Consider the following adjustments:

### In both server.py and client.py:
- Replace HOST = '127.0.0.1' with the public IP address or domain name of your server.
- Choose a port number that is open and not used by other services.





