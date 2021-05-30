import zmq
import time

host = "127.0.0.1"
port = "5001"

# Creates a socket instance
context = zmq.Context()
socket = context.socket(zmq.DEALER)
socket.setsockopt(zmq.IDENTITY, str("SenderID").encode())

# Connects the socket to a predefined port on localhost
socket.connect("tcp://{}:{}".format(host, port))

# Sends a multipart message
socket.send(b"hello")
