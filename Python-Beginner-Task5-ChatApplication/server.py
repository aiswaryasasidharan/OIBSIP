import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5555

clients = {}
lock = threading.Lock()


def timestamp():
    return datetime.now().strftime("%H:%M")


def broadcast(message, sender=None):
    with lock:
        for client in list(clients):
            if client != sender:
                try:
                    client.send(message.encode())
                except:
                    remove_client(client)


def remove_client(client):
    with lock:
        username = clients.pop(client, None)

    if username:
        try:
            client.close()
        except:
            pass

        message = f"[{timestamp()}] {username} disconnected."
        print(message)
        broadcast(message)


def handle_client(client):
    try:
        username = client.recv(1024).decode().strip()

        if not username:
            username = "User"

        with lock:
            clients[client] = username

        message = f"[{timestamp()}] {username} joined the chat."
        print(message)
        broadcast(message, client)

        while True:
            data = client.recv(1024)

            if not data:
                break

            message_text = data.decode().strip()

            if message_text:
                message = f"[{timestamp()}] {username}: {message_text}"
                print(message)
                broadcast(message, client)

    except (ConnectionResetError, ConnectionAbortedError):
        pass

    finally:
        remove_client(client)


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen()

    print(f"Chat server started on {HOST}:{PORT}")
    print("Waiting for clients...")

    while True:
        client, address = server.accept()

        print(f"New connection from {address}")

        thread = threading.Thread(
            target=handle_client,
            args=(client,),
            daemon=True
        )

        thread.start()


if __name__ == "__main__":
    start_server()