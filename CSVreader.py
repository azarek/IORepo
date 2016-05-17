import csv
import operator

znakOddzielajacy = input()
sciazkaDoPliku = input()

nadawcy = []
odbiorcy = []

plik = open(sciazkaDoPliku)
czytnik = csv.reader(plik, delimiter = znakOddzielajacy)

for id_wiersza, wiersz in enumerate(czytnik):
    if id_wiersza == 0:
        continue
    nadawcy.append((int(wiersz[0]), int(wiersz[3])))
    odbiorcy.append((int(wiersz[1]), int(wiersz[3])))

nadawcyDic = dict()
odbiorcyDic = dict()

for i in range(0,len(nadawcy)):
    if nadawcy[i][0] not in nadawcyDic:
        nadawcyDic[nadawcy[i][0]] = 0
    nadawcyDic[nadawcy[i][0]] += 1

for i in range(0,len(odbiorcy)):
    if odbiorcy[i][0] not in odbiorcyDic:
        odbiorcyDic[odbiorcy[i][0]] = 0
    odbiorcyDic[odbiorcy[i][0]] += 1

a1 = sorted(nadawcyDic.items())
b1 = sorted(a1, key = operator.itemgetter(1), reverse = True)
a2 = sorted(odbiorcyDic.items())
b2 = sorted(a2, key = operator.itemgetter(1), reverse = True)


nadawca = b1[0][0]
odbiorca = b2[0][0]

listaNadawcy = []
sumaNadawcy = 0

for i in range (0,len(nadawcy)):
    if nadawcy[i][0] == nadawca:
        a = int(nadawcy[i][1])
        listaNadawcy.append(a)

for i in listaNadawcy:
    sumaNadawcy = sumaNadawcy + i

listaOdbiorcy = []
sumaOdbiorcy = 0

for i in range (0,len(odbiorcy)):
    if odbiorcy[i][0] == odbiorca:
        a = int(odbiorcy[i][1])
        listaOdbiorcy.append(a)

for i in listaOdbiorcy:
    sumaOdbiorcy = sumaOdbiorcy + i

n = int(nadawca)
o = int(odbiorca)

if sumaOdbiorcy == sumaNadawcy:
    if n > o:
        print(str(n)+":",sumaNadawcy)
    else:
        print((o)+":",sumaOdbiorcy)
else:
    print(str(n) + ": ",sumaNadawcy)
    print(str(o)+": ",sumaOdbiorcy)
