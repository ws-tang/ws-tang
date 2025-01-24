"""
Section: 2.1.1.1

Estimated time: 20-30 minutes

Level of difficulty: Easy

Objectives
Learn how to:

    use the socket module and its basic functionalities;
    manage simple http connections.

Scenario
We want you to write a simple CLI (Command Line Interface) tool which can be used in order to diagnose the current status of a particular http server. The tool should accept one or two command line arguments:

    (obligatory) the address (IP or qualified domain name) of the server to be diagnosed (the diagnosis will be extremely simple, we just want to know if the server is dead or alive)
    (optional) the server's port number (any absence of the argument means that the tool should use port 80)
    use the HEAD method instead of GET — it forces the server to send the full response header but without any content; it's enough to check if the server is working properly; the rest of the request remains the same as for GET.

We also assume that:

    the tool checks if it is invoked properly, and when the invocation lacks any arguments, the tool prints an error message and returns an exit code equal to 1;
    if there are two arguments in the invocation line and the second one is not an integer number in the range 1..65535, the tool prints an error message and returns an exit code equal to 2;
    if the tool experiences a timeout during connection, an error message is printed and 3 is returned as the exit code;
    if the connection fails due to any other reason, an error message appears and 4 is returned as the exit code;
    if the connection succeeds, the very first line of the server’s response is printed. 

Hints:

    to access command line arguments, use the argv variable from the sys module; its length is always one more than the actual number of arguments, as argv[0] stores your script's name; this means that the first argument is at argv[1] and the second at argv[2]; don't forget that the command line arguments are always strings!
    returning an exit code equal to n can be achieved by invoking the exit(n) function.

Assuming that the tool is placed in a source file name sitechecker.py, here are some real-use cases:

"""

import sys
import socket


def print_usage():
    print("sitechecker.py Usage")
    print("========================================")
    print("    python sitechecker.py server_addr [port_number]\n")
    print("where:")
    print("    server_addr: the site FQDN or IP address.")
    print("    port_number: (optional) the site port number. The default is 80.")
    print("\n")

# Write your code here.
arg_num = len(sys.argv)
if arg_num not in [2, 3]:
    print("Invalid number of arguments.\n")
    print_usage()
    exit(1)

server_addr = sys.argv[1]
if arg_num == 3:
    try:
        server_port = int(sys.argv[2])
        if server_port < 1 or server_port > 65535:
            raise ValueError("Invalid port- the port must be between 1 and 65535.\n")
    except ValueError:
        print("The port must be a number between 1 and 65535.\n")
        print_usage()
        exit(2)
else:
    server_port = 80

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_addr, server_port))
    sock.send(b"HEAD / HTTP/1.1\r\nHost: " +
              bytes(server_addr, "utf8") +
              b"\r\nConnection: close\r\n\r\n")
    reply = sock.recv(10000)
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
except socket.timeout:
    print("The connection failed due to timeout. Check the server address.\n")
    print_usage()
    exit(3)
except Exception as e:
    print(f"An unexpected error occurred: {e}\n")
    print_usage()
    exit(4)

print(repr(reply))
