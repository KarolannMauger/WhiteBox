from socket import socket, AF_INET, SOCK_DGRAM
import test_led_couleur
import queue
import threading

PORT: int = 9090
BUFFER_SIZE: int = 1024

data_queue = queue.Queue()

socket_local: socket = socket(AF_INET, SOCK_DGRAM)
adr_local: tuple = ("", PORT)
socket_local.bind(adr_local)
print(f"On attend les messages UDP entrants au port {PORT}...\n")
                
couleurs_proxemie = test_led_couleur.charger_couleurs_json()



def msg_from_udp():
    while True:
        buffer, adr_local = socket_local.recvfrom(BUFFER_SIZE)

        msg: int = buffer.decode()
            
        data_queue.put(msg)
        

        print(f"> {msg}\n", end="")


led_thread = threading.Thread(target=test_led_couleur.openLed, args=(data_queue, couleurs_proxemie), daemon=True).start()



if __name__ == "__main__":
    try:
        #data = data_queue.get_nowait()
        msg_from_udp()
    except KeyboardInterrupt:
        print("\nFin du programme")
    finally:
        test_led_couleur.close_led()
        socket_local.close()