
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 4954))
server.listen()

clients = []
usernames = []

def server_post(message):
    for client in clients:
        client.send(message)

def client_post(chat):
    for client in clients:
        client.send(chat)
def receive():
    while True:
        client, address = server.accept()
        print(f'\nConnected with: {address}.')

        client.send('Please enter your username: '.encode('ascii'))
        username = client.recv(1024).decode('ascii')
        usernames.append(username)
        clients.append(client)

        print(f'Clients username is: {username}')
        server_post(f'\n{username}has joined the chat\n'.encode('ascii'))
        client.send(f'\nWelcome to the chat room, {username}'.encode('ascii'))
        # client_post(f'{username}: \n'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

def handle(client):
    while True:
        
        try:
            message = client.recv(1024)
            server_post( message)
        except:
            index = clients.index(clients)
            clients.remove(clients)
            client.close()
            username = usernames[index]
            server_post(f'\nGood bye, {username}.')
            usernames.remove(username)
            break


def main():
    receive()

if __name__ == "__main__":
    main()





