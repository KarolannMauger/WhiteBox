from socket import socket, AF_INET, SOCK_DGRAM
from time import sleep

PORT: int = 9090
ADDR = ""

if __name__ == "__main__":
    try: 
        sock: socket = socket(AF_INET, SOCK_DGRAM)
        
        dest_addr = (ADDR, PORT)
        
        while True:
            sock.send("".encode(), dest_addr)
            sleep(0.5)
            

    except Exception as error:
        print(error)
        
    finally:
        sock.close()