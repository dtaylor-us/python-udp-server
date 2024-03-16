# Simple UDP Chat Application

Overview of a simple chat application using the User Datagram Protocol (UDP) in Python. The application is divided into two main scripts: a server script and a client script. This application enables basic message exchange between a client and a server over a network.

## Overview

The application uses UDP, a connectionless protocol, to send and receive messages. This choice allows for simple, non-persistent communication channels that do not require a continuous connection, making it suitable for lightweight messaging applications.

### Server Script

The server script sets up a UDP socket and listens for messages from any client. Upon receiving a message, it prints the message to the console and prompts the user (server-side) to input a response. This response is then sent back to the client.

Key Features:
- Binds a UDP socket to a specified hostname and port.
- Receives messages from clients and decodes them from ASCII.
- Allows the server user to respond to each message.

### Client Script

The client script allows users to send messages to the server. It sends a user-inputted message to the server and waits for a response. Upon receiving the response, it prints the message to the console.

Key Features:
- Connects to the server via a UDP socket.
- Sends messages inputted by the user to the server.
- Receives and prints responses from the server.

## Requirements

- Python 3.x

## Usage

### Server

1. Run the server script on the desired machine.
2. Keep the terminal open and wait for messages from clients.

### Client

1. Run the client script on the machine from which you wish to send messages.
2. Enter messages into the console. The response from the server will be displayed after each message.

## Running the Application

To run the server, open a terminal and execute:

```bash
python server_script.py
```

To run the client, open another terminal and execute:

```bash
python client_script.py
```

## Example Interaction

- Server Terminal:

```
Listening at ('127.0.0.1', 3000)
The client at ('127.0.0.1', random_port) says 'Hello, server!'
Input message to send to client: Hello, client!
```

- Client Terminal:

```
Input message to send to server: Hello, server!
The server replied with 'Hello, client!'
```

## Closing the Application

To close the server or client, simply interrupt the process by pressing `CTRL+C` in the terminal. The client script includes a graceful shutdown that closes the socket upon interruption.

## Note

This application is designed for educational purposes and demonstrates basic UDP communication in Python. It is not intended for production use. UDP does not guarantee message delivery, order, or integrity, so this application may not be suitable for critical communication needs.
