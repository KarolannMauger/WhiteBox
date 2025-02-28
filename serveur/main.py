from socket import socket, AF_INET, SOCK_DGRAM

PORT: int = 9090
BUFFER_SIZE: int = 1024


if __name__ == "__main__":
    try:
        socket_local: socket = socket(AF_INET, SOCK_DGRAM)

        adr_local: tuple = ("", PORT)

        socket_local.bind(adr_local)

        print(f"On attend les messages UDP entrants au port {PORT}...\n")

        while True:
            buffer, adr_local = socket_local.recvfrom(BUFFER_SIZE)

            msg: str = buffer.decode()

            print(f"> {msg}\n", end="")

    finally:
        socket_local.close()