import zmq
import time

host = "127.0.0.1"
port = "5001"

# Creates a socket instance
context = zmq.Context()
socket = context.socket(zmq.ROUTER)

# Binds the socket to a predefined port on localhost
socket.bind("tcp://{}:{}".format(host, port))

# Recvs a multipart message
print(socket.recv_multipart())
