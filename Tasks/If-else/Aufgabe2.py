dienstalter = int(input("Anzahl der Dienstjahre: "))
praemie = 0
lebensalter = int(input("Geben sie ihr Alter an: "))

if dienstalter < 1:
    print("Sie erhalten keine Prämie")
    
elif dienstalter >= 1 and dienstalter < 6:
    praemie += 200
    print(f"Sie erhalten eine Prämie von {praemie} euro")
    
else:
    praemie += 80 
    praemie += (dienstalter * 20)
    
    if lebensalter > 50:
        praemie += 50
    print(f"Sie erhalten eine Prämie von {praemie} euro")
    
