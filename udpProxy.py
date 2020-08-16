#
#   PxVS-Frames Duplicator
#   s.kloniecki@outlook.com
#
import socket

# Initial values
bufSize = 8192
targetHost = "127.0.0.1"
targetPorts = [9002, 9003]
listenHost = "0.0.0.0"
listenPort = 9001


def forward(data, port):
    print("Forwarding: '%s' from port %s" % (data, port))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("localhost", port))  # Bind to the port data came in on 9001
    for destinationPort in targetPorts:
        sock.sendto(data, (targetHost, destinationPort))


def listen(host, port):
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    listen_socket.bind((host, port))
    print("*** Listening on %s:%s" % (host, port))
    while True:
        data, addr = listen_socket.recvfrom(bufSize)
        forward(data, addr[1])  # data and port


# main
try:
    listen(listenHost, listenPort)
except AttributeError as err:
    print(err)
except ConnectionError as err:
    print(err)
except ConnectionAbortedError as err:
    print(err)
except ConnectionRefusedError as err:
    print(err)
except BufferError as err:
    print(err)
except OSError as err:
    print(err)
