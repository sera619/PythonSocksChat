import errno
import select
import socket
import sys

print(f"""
	 .oooooo..o   .oooo.   ooooooooo.         .o     .oooo.               .oooo.
	d8P'    `Y8 .dP""Y88b  `888   `Y88.     .d88   .dP""Y88b            .dP""Y88b
	Y88bo.            ]8P'  888   .d88'   .d'888         ]8P'  .ooooo.        ]8P'
	 `"Y8888o.      <88b.   888ooo88P'  .d'  888       <88b.  d88' `88b     <88b.
	     `"Y88b      `88b.  888`88b.    88ooo888oo      `88b. 888   888      `88b.
	oo     .d8P o.   .88P   888  `88b.       888   o.   .88P  888   888 o.   .88P
	8""88888P'  `8bd88P'   o888o  o888o     o888o  `8bd88P'   `Y8bod8P' `8bd88P'  """)
print(f"\n************************************************************************************")
print(f"\n*                             Socket based ChatTerminal                            *")
print(f"\n*             _     _     _     _     _     _       _     _     _     _            *")
print(f"\n*            / \   / \   / \   / \   / \   / \     / \   / \   / \   / \           *")
print(f"\n*           ( C ) ( L ) ( I ) ( E ) ( N ) ( T )   ( S ) ( I ) ( D ) ( E )          *")
print(f"\n*            \_/   \_/   \_/   \_/   \_/   \_/     \_/   \_/   \_/   \_/           *")
print(f"\n************************************************************************************")
print(f"\n*                             Copyright of S3R43o3, 2021                           *")
print(f"\n*                           https://www.Github.com/sera619)                        *")
print(f"\n*                                 No System is Safe                                *")
print(f"\n*                                                                                  *")
print(f"\n************************************************************************************")

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

my_username = input("Choose a Username: ")

# Create a socket
# socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
# socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a given ip and port
client_socket.connect((IP, PORT))

# Set connection to non-blocking state, so .recv() call won;t block, just return some exception we'll handle
client_socket.setblocking(False)

# Prepare username and header and send them
# We need to encode username to bytes, then count number of bytes and prepare header of fixed size, that we encode to bytes as well
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

while True:

    # Wait for user to input a message
    message = input(f'{my_username} > ')

    # If message is not empty - send it
    if message:

        # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)

    try:
        # Now we want to loop over received messages (there might be more than one) and print them
        while True:

            # Receive our "header" containing username length, it's size is defined and constant
            username_header = client_socket.recv(HEADER_LENGTH)

            # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()

            # Convert header to int value
            username_length = int(username_header.decode('utf-8').strip())

            # Receive and decode username
            username = client_socket.recv(username_length).decode('utf-8')

            # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any length)
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            # Print message
            print(f'{username} > {message}')

    except IOError as e:
        # This is normal on non blocking connections - when there are no incoming data error is going to be raised
        # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
        # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
        # If we got different error code - something happened
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()

        # We just did not receive anything
        continue

    except Exception as e:
        # Any other exception - something happened, exit
        print('Reading error: '.format(str(e)))
        sys.exit()
