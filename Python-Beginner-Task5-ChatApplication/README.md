# Chat Application – Python

## Project Overview

This project is a simple real-time two-user chat application developed as part of the Oasis Infobyte Python Programming Internship.

The application uses Python socket programming and threading to allow two clients to communicate with each other through a local server.

## Features

* Server that listens for client connections
* Client that connects to the server
* Real-time bidirectional messaging
* Timestamp displayed with each message
* Username displayed with messages
* Multiple clients can connect to the server
* Graceful client disconnection handling
* Runs locally using `localhost`

## Technologies Used

* Python
* socket
* threading
* datetime

## How It Works

The application consists of two main scripts:

### Server

`server.py` creates a TCP socket and listens for incoming client connections.

It receives messages from connected clients and broadcasts them to the other connected clients.

### Client

`client.py` connects to the local server and allows the user to send and receive messages in real time.

A separate thread is used to receive incoming messages while the user can continue typing messages.

## Project Structure

```text
Python-Beginner-Task3-ChatApplication/
│
├── server.py
├── client.py
├── requirements.txt
└── README.md
```

## How to Run

### Step 1 – Start the Server

Open a terminal and run:

```bash
python server.py
```

The server will start on:

```text
127.0.0.1:5555
```

### Step 2 – Start the First Client

Open another terminal and run:

```bash
python client.py
```

Enter a username when prompted.

### Step 3 – Start the Second Client

Open another terminal and run:

```bash
python client.py
```

Enter another username.

The two clients can now exchange messages in real time.

## Example

Client 1:

```text
Enter your name: Aiswarya
Connected to the chat!
Type your message. Type 'exit' to leave.

You: Hello
```

Client 2:

```text
Enter your name: Friend
Connected to the chat!

[21:30] Aiswarya: Hello
You: Hi Aiswarya
```

## Disconnecting

To leave the chat, type:

```text
exit
```

The other connected client will be notified that the user has disconnected.

## Security and Privacy Note

This is a beginner-level local socket chat application intended for learning purposes.

Messages are transmitted through a local TCP connection and are not end-to-end encrypted. The application does not provide authentication, persistent message storage, or encryption.

The application is designed to run on `localhost` for testing and learning.
