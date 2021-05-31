import re   #Per utilizzare le Regular Expression

terms = {}
numbersArr = []
uids ={}
numbers = {}

# Si apre il file indicato in modalità rb, il che significa che stiamo leggendo il binario senza traduzione di 
# interruzione di riga.
meshFile = 'C:\\Users\\lruggiero\\Documents\\Consulcesi\\python\\d2021.bin'
with open(meshFile, mode='rb') as file:
    mesh = file.readlines()

# Utilizziamo dei file di output dove memorizzare i risultati della procedura
outputFile = open('C:\\Users\\lruggiero\\Documents\\Consulcesi\\python\\mesh.txt', 'w')
outputNumberFile = open('C:\\Users\\lruggiero\\Documents\\Consulcesi\\python\\mesh_numbers.txt', 'w')
outputListFile = open('C:\\Users\\lruggiero\\Documents\\Consulcesi\\python\\mesh_list.txt', 'w')

numberStr = ''

# Cicliamo il file di input
for line in mesh:
    # L'espressione regolare "MH = (. +) $" ci dice fondamentalmente di trovare il letterale "MH ="" seguito da 
    # almeno un carattere. "(.)" significa qualsiasi carattere e "+"" significa che deve essere uno o più caratteri: 
    # tale pattern restituirà tutto quello trovato fino alla fine della riga "($)".
    # Si usa "b" invece di "r", per l'espressione regolare, poiché stiamo applicando il pattern su un oggetto 
    # byte e non su un oggetto stringa
    # La parentesi intorno a ". +", ovvero (. +), è un gruppo di cattura, con il quale possiamo recuperare il 
    # risultato.
    # Le istruzioni "if" ​​è che alcune righe non inizieranno né con "MH =" né con "MN =".
    # Per il termine MeSH catturato e il numero MeSH, creiamo una nuova coppia chiave-valore per un oggetto 
    # dizionario "numbers [str (number)] = term".
    # È importante notare che un singolo termine MeSH potrebbe avere più di un numero MeSH. Quindi concateniamo ogni 
    # nuovo numero MeSH con il termine pertinente in una stringa
    # Alla fine avremo un oggetto dizionario con coppie chiave-valore che consistono in un termine MeSH 
    # come chiave e la raccolta di concatenazione di tutti i numeri MeSH corrispondenti come valore.

    #Righe che iniziano con "MH = "
    meshTerm = re.search(b'MH = (.+)$', line)
    if meshTerm:
        term = meshTerm.group(1)            
    
    #Righe che iniziano con "MN = "
    meshNumber = re.search(b'MN = (.+)$', line)
    if meshNumber:
        number = meshNumber.group(1)
        if(numberStr != ''):
            numberStr = numberStr + ' ' + number.decode('utf-8')
        else:
            numberStr = number.decode('utf-8')
        
        numbers[number.decode('utf-8')] = term.decode('utf-8')
        numbersArr.append(number.decode('utf-8'))

        if term in terms:
            terms[term] = terms[term] + ' ' + number.decode('utf-8')
        else:
            terms[term] = number.decode('utf-8')

    #Righe che iniziano con "UI = "
    uidTerm = re.search(b'UI = (.+)$', line)
    if uidTerm:
        uid = uidTerm.group(1)
        uids[uid] = numberStr
        numberStr = ''

#Stampiamo i risultati dell'elaborazione UI - MN
#print(uids, file=outputFile)

#Filtering UI
#print(uids[b'D042361'])

#Sorting del dictionary UI - MN e stampa su file
sort_orders = sorted(uids.items(), key=lambda x: x[1], reverse=False)
for i in sort_orders:
    print(i[0], i[1], file=outputFile)

#Sorting e stampa dei soli Numbers MN
numbersArr.sort(reverse=False)
print(numbersArr, file=outputNumberFile)

#Costruzione di una Lista MH - MN e stampa su file
meshNumberList = []
meshTermList = terms.keys()
for term in meshTermList:
    item_list = terms[term].split(' ')
    for phrase in item_list:
        meshNumberList.append(phrase)
 
meshNumberList.sort()
 
used_items = set()
for item in meshNumberList:
    if numbers[item] not in used_items:
        print(numbers[item], '\n', item, file=outputListFile)
        used_items.add(numbers[item])
    else:
        print(item, file=outputListFile)