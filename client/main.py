from socket import socket, AF_INET, SOCK_DGRAM
from time import sleep
from capteur_ultrasonic import distance
from pigpio import pi, OUTPUT, INPUT

SLEEP: int = 0.10
PORT: int = 9090
ADDR: str = "10.10.21.138"
TRIG: int = 15
ECHO: int = 14

if __name__ == "__main__":
    pi = pi()

    pi.set_mode(TRIG, OUTPUT)
    pi.set_mode(ECHO, INPUT)
    try:
        sock: socket = socket(AF_INET, SOCK_DGRAM)
        
        dest_addr: tuple = (ADDR, PORT)
        
        while True:
            sock.sendto(str(distance(pi, TRIG, ECHO)).encode(), dest_addr)
            sleep(SLEEP)
            

    except (Exception | KeyboardInterrupt) as error:
        print(error)
        
    finally:
        pi.stop()
        sock.close()
        