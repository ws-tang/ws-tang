"""
Section: 2.1.1.4

Estimated time: 20-30 minutes

Level of difficulty: Medium

Objectives
Learn how to:

    use the requests module facilities;
    interpret server responses.

Scenario
Now we want to you to return to the issues discussed in lab #1. In fact, you need to implement exactly the same functionality as you embedded in your code previously, but this time you have to use the requests module instead of the socket module. Everything else should remain the same: the command line arguments and outputs have to be indistinguishable.

Hint: use the head() method instead of get(), as you don't need the whole root document the server sends to you — the header is enough to test whether or not the server is responding. Fortunately, head() has exactly the same interface as get(). Don't forget to handle all needed exceptions — don't leave your user without any clear explanations about anything that went wrong.

"""

import sys
import requests


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

req_url = "http://" + server_addr + ":" + str(server_port)
print(req_url)

try:
    reply = requests.head(req_url)
    print(reply.status_code)
except requests.RequestException:
    print("Communication error")
else:
    if reply.status_code == requests.codes.ok:
        print(reply.text)
    elif reply.status_code >= 300 and reply.status_code <= 308:
        print(reply.headers)
    else:
        print(f"Server error with the status code [{reply.status_code}]")
