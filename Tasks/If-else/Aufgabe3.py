
def ist_schaltjahr(jahr):
    if jahr % 4 == 0:
        if jahr % 100 == 0:
            if jahr % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else: 
        return False

# Benutzereingabe abfragen
eingabe = int(input("Geben Sie eine Jahreszahl ein: "))

# Überprüfen, ob es sich um ein Schaltjahr handelt 
if ist_schaltjahr(eingabe):
    print(eingabe, "ist ein Schaltjahr.")
else: 
    print(eingabe, "ist kein Schaltjahr.")
