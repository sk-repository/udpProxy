#
#   PxVS-Frames Duplicator
#   s.kloniecki@outlook.com
#
import socket

# set these values
bufsize = 8192
target_host = "127.0.0.1"
target_port1 = 9002
target_port2 = 9003
listen_host = "192.168.204.49"
listen_port = 9001


def forward(data, port):
    print("Forwarding: '%s' from port %s" % (data, port))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("localhost", port))  # Bind to the port data came in on 9001
    sock.sendto(data, (target_host, target_port1))  # Send data to 9002
    sock.sendto(data, (target_host, target_port2))  # Send data to 9003


def listen(host, port):
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    listen_socket.bind((host, port))
    print("*** Listening on %s:%s" % (host, port))
    while True:
        data, addr = listen_socket.recvfrom(bufsize)
        forward(data, addr[1])  # data and port1


# main
try:
    listen(listen_host, listen_port)
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
