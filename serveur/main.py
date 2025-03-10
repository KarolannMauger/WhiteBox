from socket import socket, AF_INET, SOCK_DGRAM
import led_color_control
import queue
import threading

#Constants
PORT: int = 9090
BUFFER_SIZE: int = 1024

#Create a queue to store the data
data_queue = queue.Queue()

#Create a socket to receive the messages from the client UDP
socket_local: socket = socket(AF_INET, SOCK_DGRAM)
adr_local: tuple = ("", PORT)
socket_local.bind(adr_local)
print(f"On attend les messages UDP entrants au port {PORT}...\n")
 

#Load the colors from the json file               
couleurs_proxemie = led_color_control.charger_couleurs_json()


#This thread opens the LED strip
led_thread = threading.Thread(target=led_color_control.openLed, args=(data_queue, couleurs_proxemie), daemon=True).start()

"""
    This function receives the messages from the client UDP
"""
def msg_from_udp():
    while True:
        buffer, adr_local = socket_local.recvfrom(BUFFER_SIZE)

        msg: int = buffer.decode()
            
        data_queue.put(msg)
        

        print(f"> {msg}\n", end="")

"""
    This is the main function
"""
if __name__ == "__main__":
    try:
        msg_from_udp()
    except KeyboardInterrupt:
        print("\nFin du programme")
    finally:
        led_color_control.close_led()
        socket_local.close()