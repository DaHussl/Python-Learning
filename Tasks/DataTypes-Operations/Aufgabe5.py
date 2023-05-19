#boolsche Variable
a = True 
varName = f"{a=}".split("a")[0]

#ganzzahlige Variable 
b = 10 
varName = f"{b=}".split("b")[0]

#Fliegkommavariable 
c = 17,3 
varName = f"{c=}".split("c")[0]

#Textvariable 
d = "Das ist ein Text"
varName = f"{d=}".split("d")[0]

print(f"Die Variable a hat den Wert {a} und ist vom Typ {type(a)}.")
print(f"Die Variable b hat den Wert {b} und ist vom Typ {type(b)}.")
print(f"Die Variable c hat den Wert {c} und ist vom Typ {type(c)}.")
print(f"Die Variable d hat den Wert {d} und ist vom Typ {type(d)}.")

