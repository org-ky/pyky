#Lista eterogenea
a = [1, "pippo", 4.5, "pluto"]
print(a[0])
for i in range(0, len(a)):
    print(a[i])

for l in a:
    print(l)

#Lista omogenea di valori numerici
b = [1, 3.5, -6.0, 5]
b.append(46)
i = len(b) - 1
print("Rimuove l\'elemento ", i, " ", b.pop(i))

#La seguente funzione di ordinammento sulle liste funziona solo se gli elementi in
#essa contenuti sono compatibili
b.sort()
print(b)
b[1] = 15
b.sort()
print(b)

#Lista omogenea di valori stringa
c = ["abaco", "rimessa", "cielo", "mantello"]
c.sort()
print(c)
