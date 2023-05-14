einsatz1 = int(input("Einsatz von Person 1 eingeben: "))
einsatz2 = int(input("Einsatz von Person 2 eingeben: "))
einsatz3 = int(input("Einsatz von Perons 3 eingeben: "))
gesamt = int(input("Bitte den zu verteilenden Gewinn eingeben: "))

gewinnMult = gesamt / (einsatz1 + einsatz2 + einsatz3)
gewinn1 = gewinnMult * einsatz1
gewinn2 = gewinnMult * einsatz2
gewinn3 = gewinnMult * einsatz3

print (f"Person 1 erhält: {gewinn1}")
print (f"Person 2 erhält: {gewinn2}")
print (f"Person 3 erhält: {gewinn3}")
