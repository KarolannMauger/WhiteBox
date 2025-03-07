import json
import time
from rpi_ws281x import PixelStrip, Color

LED_COUNT = 50        
LED_PIN = 12
strip = PixelStrip(LED_COUNT, LED_PIN)
strip.begin()

def charger_couleurs_json(fichier="couleurs.json"):
   with open(fichier, "r") as file:
       couleurs = json.load(file)
   return {int(k): tuple(v) for k, v in couleurs.items()}


def get_couleur_dict(distance, couleur_dict):
    return couleur_dict[200] if distance >= 200 else couleur_dict[(distance//10)*10]


#######################################################################MAIN###########################################################################################################

def openLed(data_queue, couleurs_proxemie):
    while True:
        distances_test = data_queue.get()
        print(distances_test)
        couleur = get_couleur_dict(int(distances_test), couleurs_proxemie)
        r, g, b = couleur
        for i in range(LED_COUNT):
            strip.setPixelColor(i, Color(r, g, b))
        strip.show()

def close_led():
    for i in range(LED_COUNT):
        strip.setPixelColor(i, Color(0,0,0))
    strip.show()
