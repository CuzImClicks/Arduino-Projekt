import pyfirmata
import time
from clicks_util import logger
import logging
'''
ich benutze Python mit dem Programm pyfirmata, das wird dazu benutzt um die Kommunkation zwischen
Python und Arduino zu ermöglichen. Um Firmata einzurichten muss man:
Arduino IDE: 
Datei
    Beispiele
        Firmata
            StandartFirmata
'''
# Ein Logger der die Nachrichten die das Programm ausgibt ein bisschen schöner macht und Informationen
# wie Uhrzeit hinzufügt
lg = logging.getLogger("Arduino Main")

# erstelle ein "board" aus der Klasse Arduino(Uno)
# COM3 ist das Ausgabeziel
board = pyfirmata.Arduino("COM3")

lg.info("Started Arduino")

# definiere eine Funktion die zwei Argumente nimmt
# den Pin auf dem Arduino Digital bereich und die Zeit die gewartet werden soll


def switch(pin, tm):
    # schreibe auf den pin eine 1, also schalte ich ihn an
    board.digital[int(pin)].write(1)
    lg.info(f"Wrote 1 to digital pin {int(pin)}, waiting for {tm} seconds")
    time.sleep(int(tm)) # tm sekunden warten
    board.digital[int(pin)].write(0) # schreibe auf den pin eine 0, also schalte ich ihn aus
    lg.info(f"Wrote 0 to digital pin {int(pin)}, waiting for {tm} seconds")
    time.sleep(int(tm)) # tm sekunden warten


t = 1
# gehe in einen unendlichen Kreislauf der läuft bis ich ihn anhalte
while True:
    switch(13, t)


