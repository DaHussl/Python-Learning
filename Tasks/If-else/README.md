# Aufgabe 1
Erstellen Sie ein Programm, welches bei der Eingabe der Schulnote den dazugehörigen Wortlaut ausgibt.
Bps.:
```
Note 6 -> ungenügend
```

# Aufgabe 2
Eine Firma gewährt ihren Angestellten unter folgenden Bedingungen zu Weihnachten eine Prämie: Beträgt das Dienstalter (= Anzahl der Dienstjahre) weniger als ein Jahr, wird keine Prämie gegeben; beträgt es mindestens ein Jahr aber weniger als sechs Jahre, besteht die Prämie aus 200 €. Ist der Mitarbeiter sechs oder mehr Jahre bei der Firma, bekommt er 80 € und dazu für jedes Dienstjahr 20 €. Ist er im letzteren Fall außerdem älter als 50 Jahre, so erhält er noch eine Zulage von 50 €. Wie hoch ist die Prämie? Legen Sie zunächst zwei Variablen an, in der das Dienstalter und das Alter gespeichert wird. Anschließend soll je nach Variableninhalt der entsprechende Wortlaut ausgegeben werden.

Setzten Sie den Algorithmus danach in Python um. (duh)

# Aufgabe 3
Entwerfen Sie ein Programm, dass dem Benutzer nach Eingabe einer Jahreszahl ausgibt, ob das eingegebene Jahr ein Schaltjahr ist.

Der heute gebräuchliche gregorianische Kalender beinhaltet eine Formel mit drei Kriterien, nach denen die Jahre in Gemein- und Schaltjahre unterteilt werden:

1. Schaltjahre müssen durch 4 teilbar sein.
2. Ist das Jahr auch durch 100 teilbar, ist es kein Schaltjahr, es sei denn...
3. ...das Jahr ist ebenfalls durch 400 teilbar – dann ist es ein Schaltjahr.

# Aufgabe 4
Programmieren Sie ein Würfelspiel, das automatisch eine Ganzzahl zwischen 1 und 6 für zwei Spieler ermittelt. Anschließend soll der Gewinner ermittelt werden oder das Wort unentschieden ausgegeben werden. Gewonnen hat, wer die höhere Zahl gewürfelt hat. Falls ein Spieler mit einer Sechs gewonnen hat, soll zudem ausgegeben werden. Glückwunsch, Sieg mit einer 6.

Zusatzaufgabe: Es soll angegeben werden, ob es sich um einen knappen Sieg (Augenzahl ist nur maximal 1 höher) oder um einen deutlichen Sieg handelt.

Hinweis: Informieren Sie sich im Internet, wie in Python eine [Zufallszahl](https://www.w3schools.com/python/ref_random_randint.asp) zwischen 1 und 6 erzeugt werden kann.

# Aufgabe 5
Drei eingegebene Namen soll der Rechner aufsteigend in alphabetischer Folge sortieren und in eine Form ausgeben. Verwenden Sie hierzu keine Listen und keine Sortierfunktion. Strings können mit `<`, `>` und `==` verglichen werden. Dabei ist ein Wert kleiner, wenn der String in der alphabetischen Reihenfolge weiter vorne liegt.

# Aufgabe 6
Sie sollen ein Programm für das Würfelspiel „Mäxchen“ schreiben. Zwei Spieler geben zu Beginn Ihren Namen ein. Anschließend würfelt jeder Spieler mit zwei Würfeln (generieren Sie zwei Zufallszahlen zwischen 1 und 6). Der Wert des Wurfes wird wie folgt bestimmt:

- Wird eine 2 und eine 1 gewürfelt, hat man ein Mäxchen. Das ist der höchstmögliche Wert
- Es folgen die Paschwürfe (zwei gleiche Zahlen). Je höher der Pasch, desto besser
- Trifft keine der beiden ersten Varianten zu, wird der Wert des höherwertigen Würfels als Zehnerstelle, der des niederwertigen als Einerstelle interpretiert.

Es ergibt sich also die folgende Reihenfolge (aufsteigend nach Wertigkeit): 31, 32, 41, 42, 43, 51, 52, 53, 54, 61, 62, 63, 64, 65, 11, 22, 33, 44, 55, 66, 21

Das Programm soll den Wurfwert beider Spieler anzeigen und anschließend den Gewinner verkünden.
