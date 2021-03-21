# Un dizionario e' una sequenza di elementi , ogni elemento ha una coppia chiave, valore. 
# Le chiavi sono uniche ed i dizionari si creano usando le parentesi graffe

d = {"k1":1,"k2": "valore", 3:"val3"}
print(d[3], " ", d["k1"])
d["quattro"] = 4
print(d)

if("quattro" in d):
    print("Chiave ", "\"quattro\""," presente")
else:
    print("Chiave ", "\"quattro\"","  non presente")

if(4 not in d):
    print("Chiave ", 4, " non presente")
else:
    print("Chiave ", 4, " presente")

#Recupera gli elementi/chiavi del dizionario
for x in d.values():
    print(x)
for x in d.keys():
    print(x)
for x in d.items():
    print(x)
    print(x[0], x[1])

#Cancella un elemento del dizionario
del(d["k1"])
for x in d.items():
    print(x)

#Cancella l'intero dizionario
d.clear()
print(len(d))
for x in d.items():
    print(x)