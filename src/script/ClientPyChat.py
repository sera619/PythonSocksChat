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
# hier die richtige IP und PORT angeben die IP MUSS! in "" eingefasst eingetragen werden
# PORT ohne "" die änderungen hier müssen dann indentisch mit dem ServerPyChat.py sein
IP = "127.0.0.1"
PORT = 1234

my_username = input("Choose a Username: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((IP, PORT))

client_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

while True:

    message = input(f'{my_username} > ')

    if message:

        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)

    try:
        while True:

            username_header = client_socket.recv(HEADER_LENGTH)

            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()

            username_length = int(username_header.decode('utf-8').strip())

            username = client_socket.recv(username_length).decode('utf-8')

            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            print(f'{username} > {message}')

    except IOError as e:

        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()

        # We just did not receive anything
        continue

    except Exception as e:
        # Any other exception - something happened, exit
        print('Reading error: '.format(str(e)))
        sys.exit()
