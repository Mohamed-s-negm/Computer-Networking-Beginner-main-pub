# we import the libraries (socket) & (threading)
import socket
import threading

# We assign port number and host ip. We also put both in a tuple to be used.
HOST = socket.gethostbyname(socket.gethostname())  # the ip may change so this is better in all cases.
PORT = 4040
ADDR = (HOST,PORT)

# We initiate a socket to our server and we bind it to the port number and the host ip we have.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# This function is responsible for handling the clients
def clients(conn, addr):
    print(f"New Connection {addr} is connected...")
    i = 10   # we have 10 messages at most to be sent to the server from each client.

    while i > 0:
        i -= 1
        msg = str(conn.recv(1024), "utf-8")  # we receive the messages from the clients.
        if len(msg) > 0:   # We ensure that we have a message.
            if msg == "quit":   # "quit" is  a key for the client to close the connection.
                break
            print(f"[{addr}]  {msg}")
            remaining_messages = f"{i} messages left ..."
            conn.sendall(remaining_messages.encode("utf-8"))   # We tell the clients how many messages are left.
    # After either finishing 10 messages or using the "quit" key, the connection will be closed.
    
    conn.close()  # we close the connection.
    print(f"The client {addr} is disconnected...")
    # We see if the user wants to close the server.
    status = input("Would you like to close the server? yes / no ")
    if status.lower() == "yes":
        closure()

# this function is responsible for closing the server.    
def closure():
    print("The server is being closed...")
    server.close()
    print("The server is closed. Have a nice day!")    


# This is the starting function which is resposible for connecting the clients to the server.
def start():
    server.listen() # first, we listen to the possible connections
    print(f"Server is listenning on {HOST}")
    while True:
        try:   # for any kinds of OSErrors.
            conn, addr = server.accept()  # we accept the connection of the client
            thread = threading.Thread(target=clients, args=(conn, addr))  
            thread.start()   # Using "Threading" helps us to manage more clients in the same time
            print(f"{threading.active_count() - 1} Active Connections...")
        except OSError as err:
            print(f"Server error : {err}")
            break

# finally, we initiate the server but if there are any KeyboardInterrupt erros, the server will be closed.
print("The server is starting...")
try:
    start()
except KeyboardInterrupt:
    print("Server is disconnecting...")
finally:
    closure()

