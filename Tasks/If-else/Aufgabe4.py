import random

def wurf():
    return random.randint(1, 6)

# Würfelergebnisse für die beiden Spieler generieren
spieler1 = wurf()
spieler2 = wurf()

# Die Gewinnerzahl ermitteln
gewinnerzahl = max(spieler1, spieler2)

# Den Gewinner feststellen
if gewinnerzahl == 6:
    gewinner_text = "Glückwunsch, Sieg mit einer 6!"
else: 
    gewinner_text = "Gewinner: Spieler" + str((spieler1 > spieler2) +1 )

# Den Gewinner ausgeben
print("Spieler 1: ", spieler1)
print("Spieler 2: ", spieler2)
print("Gewinner: ", gewinner_text)

