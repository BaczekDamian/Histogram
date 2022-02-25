wprowadzonytekst = input("Wprowadz tekst: ")

#tekstowe
tablica_slow = wprowadzonytekst.split(" ")
zbior = tablica_slow
lista = [] #przechowuje dlugosc slow
for slowa in zbior:
    lista.append(len(slowa))

#numeryczne
res = [int(a) for a in wprowadzonytekst.split() if a.isdigit()]
#jesli występują liczby dodaj do res

zbiorliczb = []
for liczby in res:
        res.count(liczby)
        zbiorliczb.append(res.count(liczby)) #dodaj ilosci powtorzen do listy z liczbami
        zbior.remove(str(liczby)) #usun liczby z listy ze slowami

wynikliczb = []
for c, d in zip(zbiorliczb, res) : #zestaw 2 listy liczbowe
    wynikliczb.append("Liczba: " + str(d) + " ilość: " + str(c))  #dodaj wartosci do wynikliczb

bezpowt = sorted(list(set(wynikliczb))) #usun duplikaty elementów i posortuj

for k in bezpowt:
    print(k) #wypisz statystyke liczb

#tekstowe
lista = [] #przechowuje dlugosc slow
for slowa in zbior:
    lista.append(len(slowa))

#tekstowe
listaa = [] #zawiera ilosc powtorzen tych samych dlugosci
for litery in lista:
        lista.count(litery) #zlicz litery dla każdego słowa
        listaa.append(lista.count(litery)) #dodaj te wartosci do listy

wyniki = [] #zawiera zestawienie ilosci slow o danej dlugosci
for x, y in zip(listaa, lista) :
    wyniki.append("Słowo: " + str(y) + "-znakowe, ilość: " + str(x))

bezdpl = sorted(list(set(wyniki))) #zestawienie bez duplikatow

for i in bezdpl:
    print(i)
