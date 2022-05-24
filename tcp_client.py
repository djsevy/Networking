import socket
import threading

username = input('')
chat = (f'{username} says:')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect('127.0.0.1', 4954)

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == username:
                client.send(username.encode('ascii'))
            else:
                print(message)

        except:
            print('Oops, something went wrong! Good bye!')
            client.close()
            break

def sending():
    while True:
        chat = input(f'{username} what would you like to say? \n')
        client.send(chat.encode('ascii'))

        t1= threading.Thread(target=receive)
        t1.start()

        t2 = threading.Thread(target=sending)
        t2.start()