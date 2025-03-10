import json
import time
from rpi_ws281x import PixelStrip, Color

#LED strip configuration:
LED_COUNT = 50        
LED_PIN = 12

# Create PixelStrip object with appropriate configuration.
strip = PixelStrip(LED_COUNT, LED_PIN)
strip.begin()

"""
    This function loads the colors from the json file
"""
def charger_couleurs_json(fichier="couleurs.json"):
   with open(fichier, "r") as file:
       couleurs = json.load(file)
   return {int(k): tuple(v) for k, v in couleurs.items()}


# OLD ONE
# def get_couleur_dict_old(distance, couleur_dict):
#     return couleur_dict[200] if distance >= 200 else couleur_dict[(distance//10)*10]


"""
    NEW ONE
    This function returns the color of the LED strip according to the distance
"""
def get_couleur_dict(distance, couleur_dict):
    if distance >= 200:
        return couleur_dict[200] 
    elif distance < 10:
        return couleur_dict[10] 
    else:
        return couleur_dict[((distance // 10) + 1) * 10] 


"""
    This function opens the LED strip
"""
def openLed(data_queue, couleurs_proxemie):
    while True:
        distances_test = data_queue.get()
        print(distances_test)
        couleur = get_couleur_dict(int(distances_test), couleurs_proxemie)
        r, g, b = couleur
        for i in range(LED_COUNT):
            strip.setPixelColor(i, Color(r, g, b))
        strip.show()


"""
    This function closes the LED strip
"""
def close_led():
    for i in range(LED_COUNT):
        strip.setPixelColor(i, Color(0,0,0))
    strip.show()
    
    