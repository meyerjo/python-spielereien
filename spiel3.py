# Ratespiel

# Zufallszahl festlegen (ZAHL)
import random
ZAHL = random.randint (1,1000)
ANZAHL_VERSUCHE = 0

# Immer wiederholen
while True:
    # Nutzer eine Zahl raten lassen (EINGABE)
    while True:
        try:
            EINGABE = int(input("Bitte rate eine Zahl zwischen 1 und 1000!"))
            ANZAHL_VERSUCHE = ANZAHL_VERSUCHE + 1
            if bool(EINGABE < 1001) and bool(EINGABE > 0):
                break
        except:
            print("Bitte eine Zahl zwischen 1 und 1000 eingeben!")
    # Wenn ZAHL == EINGABE:
    # -> gewonnen -> Schluss!
    if ZAHL == EINGABE:
        print ("Herzlichen Glückwunsch!")
        break

    # Wenn ZAHL > EINGABE:
    # -> ätsch, meine Zahl ist größer! -> nochmal!
    if ZAHL > EINGABE:
        print ("ätsch, meine Zahl ist größer!")

    # Wenn ZAHL < EINGABE:
    # -> ätsch, meine Zahl ist kleiner! -> nochmal!
    if ZAHL < EINGABE:
        print ("ätsch, meine Zahl ist kleiner!")
    
# Am Ende: Zahl der Versuche ausgeben:
print ("Die Anzahl Deiner Versuche:")
print (ANZAHL_VERSUCHE)
