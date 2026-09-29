import socket
import threading

HOST = "127.0.0.1"
PORT = 5555


def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode()

            if not message:
                print("Disconnected from server.")
                break

            print("\n" + message)
            print("You: ", end="", flush=True)

        except (ConnectionResetError, ConnectionAbortedError, OSError):
            print("\nDisconnected from server.")
            break


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("Could not connect to the server.")
        print("Make sure server.py is running first.")
        return

    username = input("Enter your name: ").strip()

    if not username:
        username = "User"

    client.send(username.encode())

    thread = threading.Thread(
        target=receive_messages,
        args=(client,),
        daemon=True
    )

    thread.start()

    print("Connected to the chat!")
    print("Type your message. Type 'exit' to leave.\n")

    while True:
        try:
            message = input("You: ")

            if message.lower() == "exit":
                print("Disconnecting...")
                client.close()
                break

            if message.strip():
                client.send(message.encode())

        except (ConnectionResetError, ConnectionAbortedError, OSError):
            print("Connection lost.")
            break


if __name__ == "__main__":
    start_client()