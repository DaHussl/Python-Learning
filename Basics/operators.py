number1 = 8
number2 = 3

print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 / number2)

#Rechnen mit modulu
print(number1 % number2)

#Rechnen mit Hoch (Exponent)
print(number1 ** number2)

#Damit wird immer abgerundet 
print(number1 // number2)

# -> Jetzt kommen die schnellen Schreibweisen

#Damit wird number1 zu der Summe aus number1 und number2
number1 = (number1 + number2)
print(number1)

#Das selbe wie oben drüber 
number1 += number2
print(number1)

#Vergleich
print(number1 == number2)

#Ob sie nicht gleich sind
print(number1 != number2)

#größer - kleiner
print(number1 > number2)
print(number1 < number2)
print(number1 <= number2)
print(number1 >= number2)

#---------------------------------#
#        logical operators        # 
#---------------------------------#
    
print(True and True)   #True    
print(True and False)  #False
print(1 == 2 and 1 == 1) #False and True = False
print(2 == 2 and 1 == 1) #True and True = True
print(True or False)   #True
print(True or True)    #True
print(False or False)  #False
print(1 == 2 or 1 == 1) #False or True = True
print(1 == 1 or 2 == 2) #True or True = True
print(not True)        #False
print(not False)       #True
print(True is True)    #True
print(True is False)   #False
print(False is False)  #True
print(True is not True)#False -> das gegen teil vom "is"
print(True is not False)#True ->         -"-

#Listen
list= ["bmw","audi","mercedes","porsche"]
print("bmw" in list) #abfrage ob bmw in der Liste ist = true 
print("fiat" in list) #false
