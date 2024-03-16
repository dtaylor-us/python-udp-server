import socket

PORT = 3000
HOST = '127.0.0.1'

MAX_SIZE_BYTES = 65535  # Maximum size of a UDP datagram


def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((HOST, PORT))
    return s


def get_message():
    return input('Input message to send to server:').encode('ascii')


def send_message(s, message):
    s.send(message)


def receive_message(s):
    data, _ = s.recvfrom(MAX_SIZE_BYTES)
    text = data.decode('ascii')
    print('The server replied with {!r}'.format(text))


def close_socket(s):
    print("\nInterrupted by user. Closing socket.")
    s.close()


def main():
    s = create_socket()
    try:
        while True:
            message = get_message()
            send_message(s, message)
            receive_message(s)
    except KeyboardInterrupt:
        close_socket(s)


if __name__ == "__main__":
    main()
