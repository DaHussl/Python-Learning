rechnungsbetrag = int(input("Geben sie mir einen Rechnungsbetrag in Brutto an: "))
rabattsatz = int(input("Und nun geben sie mir einen Rabatsatz an: "))

nettobetrag = rechnungsbetrag * rabattsatz / 100
nettobetrag = rechnungsbetrag - nettobetrag
UMSATZSTEUER = nettobetrag * 19 / 100
bruttobetrag = nettobetrag + UMSATZSTEUER

print(f"Dein Nettobetrag unter der Berücksichtigung des Rabatts beträgt {nettobetrag} ")
print(f"Betrag der Umsatzsteuer beträgt {UMSATZSTEUER} ")
print(f"Somit beträgt der Bruttobetrag {bruttobetrag} ")
