import pigpio
import time

BUZZER_PIN = 18
pi = pigpio.pi()
pi.set_mode(BUZZER_PIN, pigpio.OUTPUT)

"""
    Function that will be executed in a thread to make the buzzer bip
"""
def bip(distances_queue):
    last_bip_time = time.time()
    tempo = 0.8

    while True:
        distance = distances_queue.get()
        current_time = time.time()

        if distance > 25:
            pi.write(BUZZER_PIN, 0)
            continue
        elif distance <= 10:
            pi.write(BUZZER_PIN, 1)
            continue
        elif distance > 20:
            tempo = 0.8
        elif distance > 15:
            tempo = 0.4
        else:
            tempo = 0.2

        if current_time - last_bip_time >= tempo:
            pi.write(BUZZER_PIN, 1)
            time.sleep(0.01)
            pi.write(BUZZER_PIN, 0)
            last_bip_time = current_time
        time.sleep(0.001)