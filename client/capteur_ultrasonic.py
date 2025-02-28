from pigpio import pi
from time import time, sleep
    
    
def distance(pi: pi, gpio_trigger: int, gpio_echo: int) -> int:
    try:
        # Envoyer un son
        pi.write(gpio_trigger, 1)
        sleep(0.00001)
        pi.write(gpio_trigger, 0)

        # Attendre l'echo
        debut = time()
        while pi.read(gpio_echo) == 0:
            # Break si on attend le debut de l'echo plus que 1 seconde
            if time() - debut > 1: 
                break

        # Echo arrive
        echo = time()
        while pi.read(gpio_echo) == 1:
            # Break si on attend la fin de l'écho plus que 1 seconde
            if time() - echo > 1: 
                break

        # Duree de l'echo
        duree = time() - echo
        
        return int((duree * 34300) / 2)

        
    except Exception as error:
        print(error)