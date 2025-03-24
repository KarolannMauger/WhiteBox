import json
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
def load_colors_json(fichier="colors.json"):
    with open(fichier, "r") as file:
        colors = json.load(file)
    return {int(k): tuple(v) for k, v in colors.items()}

"""
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
    This function closes the LED strip
"""
def close_led():
    for i in range(LED_COUNT):
        strip.setPixelColor(i, Color(0,0,0))
    strip.show() 
    