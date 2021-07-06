import socket
import select


HEADER_LENGTH = 10

# hier die richtige IP und PORT angeben die IP MUSS! in "" eingefasst eingetragen werden
# PORT ohne "" die änderungen hier müssen dann indentisch mit dem ClientPyChat.py schript sein
# DEFAULT Einstellungen sind für den Offline gebrauch im eigenen Netzwerk:

IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))

server_socket.listen()

sockets_list = [server_socket]

clients = {}
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
print(f"\n*           ( S ) ( E ) ( R ) ( V ) ( E ) ( R )   ( S ) ( I ) ( D ) ( E )          *")
print(f"\n*            \_/   \_/   \_/   \_/   \_/   \_/     \_/   \_/   \_/   \_/           *")
print(f"\n************************************************************************************")
print(f"\n*                             Copyright of S3R43o3, 2021                           *")
print(f"\n*                           https://www.Github.com/sera619                         *")
print(f"\n*                                 No System is Safe                                *")
print(f"\n*                                                                                  *")
print(f"\n************************************************************************************")
print(f'Listening for connections on {IP}:{PORT}...')


def receive_message(client_socket):

    try:

        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header):
            return False

        message_length = int(message_header.decode('utf-8').strip())

        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except:

        return False


while True:

    read_sockets, _, exception_sockets = select.select(
        sockets_list, [], sockets_list)

    for notified_socket in read_sockets:

        if notified_socket == server_socket:

            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)

            if user is False:
                continue

            sockets_list.append(client_socket)

            clients[client_socket] = user

            print('Accepted new connection from {}:{}, username: {}'.format(
                *client_address, user['data'].decode('utf-8')))

        else:

            message = receive_message(notified_socket)

            if message is False:
                print('Closed connection from: {}'.format(
                    clients[notified_socket]['data'].decode('utf-8')))

                sockets_list.remove(notified_socket)

                del clients[notified_socket]

                continue

            user = clients[notified_socket]

            print(
                f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            for client_socket in clients:

                if client_socket != notified_socket:

                    client_socket.send(
                        user['header'] + user['data'] + message['header'] + message['data'])

    for notified_socket in exception_sockets:

        sockets_list.remove(notified_socket)

        del clients[notified_socket]
