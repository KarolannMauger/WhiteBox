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
    ENGLISH VERSION
    This function loads the colors from the json file
"""
def load_colors_json(file="colors.json"):
    with open(file, "r") as file:
        colors = json.load(file)
    return {int(k): tuple(v) for k, v in colors.item()}

"""
FRENCH VERSION
def charger_couleurs_json(fichier="colors.json"):
   with open(fichier, "r") as file:
       couleurs = json.load(file)
   return {int(k): tuple(v) for k, v in couleurs.items()}
"""

# OLD ONE
# def get_couleur_dict_old(distance, couleur_dict):
#     return couleur_dict[200] if distance >= 200 else couleur_dict[(distance//10)*10]


"""
    ENGLISH VERSION
    NEW ONE
    This function returns the color of the LED strip according to the distance
"""
def get_color_dict(distance, color_dict):
    if distance >= 200:
        return color_dict[200] 
    elif distance < 10:
        return color_dict[10] 
    else:
        return color_dict[((distance // 10) + 1) * 10] 


"""
    ENGLISH VERSION
    This function opens the LED strip
"""
def openLed(distances_queue, proxemia_colors):
    while True:
        distances = distances_queue.get()
        print(distances)
        color = get_color_dict(int(distances), proxemia_colors)
        r, g, b = color
        for i in range(LED_COUNT):
            strip.setPixelColor(i, Color(r, g, b))
        strip.show()


"""
    ENGLISH VERSION
    This function closes the LED strip
"""
def close_led():
    for i in range(LED_COUNT):
        strip.setPixelColor(i, Color(0,0,0))
    strip.show() 
    