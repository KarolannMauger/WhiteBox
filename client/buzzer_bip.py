import pigpio
import time

BUZZER_PIN = 18
pi = pigpio.pi()
pi.set_mode(BUZZER_PIN, pigpio.OUTPUT)


def bip(distances_queue):
    last_bip_time = time.time()
    tempo = 0.8

    while True:
        distance = distances_queue.get()
        current_time = time.time()

        if distance > 30:
            pi.write(BUZZER_PIN, 0)
            continue
        elif distance <= 10:
            pi.write(BUZZER_PIN, 1)
            print(f"BIP constant distance={distance}cm")
            continue
        elif distance > 20:
            tempo = 0.8
            mode = "BIP LENT"
        elif distance > 15:
            tempo = 0.4
            mode = "BIP MOYEN"
        else:
            tempo = 0.2
            mode = "BIP RAPIDE"

        print(f"Mode : {mode} (tempo={tempo}s) distance={distance}cm")
        if current_time - last_bip_time >= tempo:
            pi.write(BUZZER_PIN, 1)
            time.sleep(0.01)
            pi.write(BUZZER_PIN, 0)
            last_bip_time = current_time
        time.sleep(0.001)