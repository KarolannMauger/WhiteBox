from socket import socket, AF_INET, SOCK_DGRAM
import led_color_control
import queue
import threading

#Constants
PORT: int = 9090
BUFFER_SIZE: int = 1024

#Create a queue to store the data
distances_queue = queue.Queue()

#Create a socket to receive the messages from the client UDP
socket_local: socket = socket(AF_INET, SOCK_DGRAM)
adr_local: tuple = ("", PORT)
socket_local.bind(adr_local)
print(f"Wating for UDP messages on port {PORT}...\n")
 

#Load the colors from the json file               
proxemia_colors = led_color_control.load_colors_json()


#This thread opens the LED strip
thread_led = threading.Thread(target=led_color_control.openLed, args=(distances_queue, proxemia_colors), daemon=True).start()

"""
    This function receives the messages from the client UDP
"""
def msg_from_udp():
    while True:
        buffer, adr_local = socket_local.recvfrom(BUFFER_SIZE)

        msg: int = buffer.decode()
            
        distances_queue.put(msg)
        

        print(f"> {msg}\n", end="")

"""
    This is the main function
"""
if __name__ == "__main__":
    try:
        msg_from_udp()
    except KeyboardInterrupt:
        print("\nEnd of the program")
    finally:
        led_color_control.close_led()
        socket_local.close()