import random

# Funktion zum Ermitteln des Wurfwerts
def get_wurf():
    wurf1 = random.randint(1, 6)
    wurf2 = random.randint(1, 6)
    return max(wurf1, wurf2) * 10 + min(wurf1, wurf2)

# Eingabe der Spielernamen
spieler1 = input("Spieler 1, bitte geben Sie Ihren Namen ein: ")
spieler2 = input("Spieler 2, bitte geben Sie Ihren Namen ein: ")

# Wurf der Spieler
wurf1 = get_wurf()
wurf2 = get_wurf()

# Ausgabe der Wurfwerte
print(f"{spieler1} hat {wurf1} gewürfelt.")
print(f"{spieler2} hat {wurf2} gewürfelt.")

# Bestimmen des Gewinners
if wurf1 == 21 and wurf2 != 21:
    gewinner = spieler1
elif wurf2 == 21 and wurf1 != 21:
    gewinner = spieler2
elif wurf1 > wurf2:
    gewinner = spieler1
elif wurf2 > wurf1:
    gewinner = spieler2
else:
    gewinner = None

# Ausgabe des Gewinners
if gewinner is not None:
    print(f"Der Gewinner ist {gewinner}!")
else:
    print("Es ist ein Unentschieden!")
