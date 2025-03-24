from pigpio import pi
from time import time, sleep
    
    
def distance(pi: pi, gpio_trigger: int, gpio_echo: int) -> int:
    try:
        # Send a sound
        pi.write(gpio_trigger, 1)
        sleep(0.00001)
        pi.write(gpio_trigger, 0)

        # Wait for the echo
        debut = time()
        while pi.read(gpio_echo) == 0:
            # Break if we wait for the beginning of the echo more than 1 second
            if time() - debut > 1: 
                break

        # Echo arrives
        echo = time()
        while pi.read(gpio_echo) == 1:
            # Break if we wait for the end of the echo more than 1 second
            if time() - echo > 1: 
                break

        # Echo duration
        duree = time() - echo
        
        return int((duree * 34300) / 2)

        
    except Exception as error:
        print(error)