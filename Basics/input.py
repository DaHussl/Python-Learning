# "input" wird die Eingabe als Variable abgespeichert 
NAME = input ("Gib mal deinen Namen ein: ")
# input ist immer str deswegen muss es in eine Zahl umgwandelt werden (mit "int()" vor dem input)
age = int(input ("Wie alt bist du: "))

print (f"Hello {NAME}, du bist {age} Jahre alt!")
print (f"Du wirst nächstes Jahr {age + 1}")

# Rechnungen:
year = 2023
birthyear = year - age
print (f"Du bist {birthyear} geboren")
