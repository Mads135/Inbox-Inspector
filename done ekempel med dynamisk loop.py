from machine import Pin
from neopixel import NeoPixel
from time import sleep

# Konfiguration
NUM_LEDS = 11  # Antal LED'er
PIN_NUM = 27    # GPIO-pin til NeoPixel data
MID_INDEX = NUM_LEDS // 2  # Midterste LED (0-indekseret)
strip = NeoPixel(Pin(PIN_NUM), NUM_LEDS)

def update_leds(score):
    """
    Opdater LED-striben baseret på en score.
    
    :param score: En værdi mellem -5 og 5. 
                  -5 er helt nederst (rød), 0 er midten (gul), 5 er helt øverst (grøn).
    """
    for i in range(NUM_LEDS):
        if i == MID_INDEX:  # Gule LED i midten
            strip[i] = (255, 255, 0)
        elif score == 5:  # Alle grønne LED'er tændt, når score er 5
            if i > MID_INDEX:
                strip[i] = (0, 255, 0)  # Grøn
            else:
                strip[i] = (0, 0, 0)  # Sluk
        elif score == -5:  # Alle røde LED'er tændt, når score er -5
            if i < MID_INDEX:
                strip[i] = (255, 0, 0)  # Rød
            else:
                strip[i] = (0, 0, 0)  # Sluk
        else:
            # Juster LED'erne afhængigt af score
            if score > 0:  # Grønne LED'er tændt opad
                if i > MID_INDEX and i <= MID_INDEX + score:
                    strip[i] = (0, 255, 0)  # Grøn
                else:
                    strip[i] = (0, 0, 0)  # Sluk
            elif score < 0:  # Røde LED'er tændt nedad
                if i < MID_INDEX and i >= MID_INDEX + score:
                    strip[i] = (255, 0, 0)  # Rød
                else:
                    strip[i] = (0, 0, 0)  # Sluk
                    
            elif score == 0:  # Når score er 0, sluk alle LED'er bortset fra den gule
                if i == MID_INDEX:
                    strip[i] = (255, 255, 0)  # Gul
                else:
                    strip[i] = (0, 0, 0)  # Sluk
                   
    strip.write()

# Starttilstand
current_score = (0)  # venter på tal fra serial
update_leds(current_score)
# loop for dynamisk opdatering
while True:
    current_score = int(input())
    update_leds(current_score)
    sleep(0.1)

