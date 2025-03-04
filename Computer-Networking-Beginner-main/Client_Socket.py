# We import the socket library
import socket

# We identify the parameters of the server we want to connect to.
#SERVER = "192.168.1.102"
SERVER = "172.21.202.133"
PORT = 4040
ADDR = (SERVER,PORT)
CONNECTION = True

# We initiate a socket to the client.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print(f"Trying to connect to{SERVER}")

# this function is resposible for sending the messages to the server
def send(msg):
    message = msg.encode("utf-8")
    client.sendall(message)

# Here, we track the messages and also add the condition to stop the connection.
while CONNECTION:
    msg = input("Input your message : ")  # the user's input message
    if msg.lower() == "quit":   # Ask the user if he wants to stop the connection.
        send(msg)
        break
    send(msg)   # We send the input message to the server.
    
    response = str(client.recv(1024), "utf-8")   # we get the server's responses.
    print(f"This was received : {response}")
    if "0 messages left ..." in response:   # when the number of the messages is 0, then the connection will be closed.
        break
    
client.close()   # we close the connection in the end.
print("You are disconnected. Have a nice day!")
