t = (1,3.5,8,10.0,"prova")
for val in t:
    print(val)

#Nelle tuple rispetto alle list non è possibile modificare il valore degli elementi:
#la loro manipolazione risulta quindi piu' rapida visto che sono “immutabili”
#t[1] = 0

t = (1,3.5,8,10.0,[1,10])
for val in t:
    print(val)

#Nel caso seguente posso modificare il valore di una sottostruttura(nell'esempio una lista)
#contenuta nella tupla
t[4][0] = 25
for val in t:
    print(val)

t[4].append(46)
for val in t:
    print(val)
