from socket import socket, AF_INET, SOCK_DGRAM
from time import sleep
from ultrasonic_sensor import distance
from pigpio import pi, OUTPUT, INPUT
import queue
import threading
import buzzer_bip
from collections import deque

SLEEP: int = 0.10
PORT: int = 9090
ADDR: str = "10.10.21.160"
TRIG: int = 15
ECHO: int = 14

distances_queue = queue.Queue()

thread_buzzer = threading.Thread(target=buzzer_bip.bip, args=(distances_queue, ), daemon=True).start()

def calculate_median(distances_list):
    median_list = sorted(distances_list)
    return median_list[2]


if __name__ == "__main__":
    pi = pi()
    pi.set_mode(TRIG, OUTPUT)
    pi.set_mode(ECHO, INPUT)
    
    distances_list = deque(maxlen=5)
    
    try:
        sock: socket = socket(AF_INET, SOCK_DGRAM)
        dest_addr: tuple = (ADDR, PORT)
        while True:
            median = 0 
            dist = distance(pi, TRIG, ECHO)
            
            if not dist > 1200:
                distances_list.append(dist)
            
            if (len(distances_list) == 5):
                median = calculate_median(distances_list)
            
            sock.sendto(str(median).encode(), dest_addr)
            distances_queue.put(median)
            print(f"Median : {median}")
            sleep(SLEEP)
        
    except (Exception | KeyboardInterrupt) as error:
        print(error)
    finally:
        pi.stop()
        sock.close()
        