#FUNKCIJA LAMBDA

def zbroj(x,y):
    return x + y

print(zbroj(5,6))

lambda x,y,t,r: ...

def pozdrav(ime = "Pero"):
    return ime
print(pozdrav())

print(pozdrav("Sanja"))

#multiplier = lambda x, factor = 2: x = "factor"
#print(multiplier(5))
#print(multiplier(5, 3))
tekst = "Ovo je neki tekst"

veliki_tekst = lambda tekst: tekst.upper()

print(veliki_tekst(tekst))

def fun(lista, fun):
    return fun(lista)

def primjeni_na_sve(lista, funkcija):
    print(funkcija) #ime i adresa odabrane funkcije
    rezultat = []
    for element in lista:
            rezultat.append(funkcija(element))
    return rezultat

lista = [1,2,3,4,5]
def uvecaj_za_pet(broj):
     return broj + 5

nova_lista = primjeni_na_sve(lista, uvecaj_za_pet)

print(nova_lista)

#s lambda funkcijama

def fun(lista2, fun):
    return fun(lista2)

def primjeni_na_sve(lista2, funkcija):
    print(funkcija) #ime i adresa odabrane funkcije
    rezultat = []
    for element in lista2:
            rezultat.append(funkcija(element))
    return rezultat

lista2 = [10,20,30,40,50]

nova_lista = primjeni_na_sve(lista2, lambda broj: broj + 5)

print(nova_lista)

#prvi nacin
def kvadriraj():
    return lambda x: x**2

kvadriraj_broj = kvadriraj()

print(kvadriraj_broj(5))

#drugi nacin
kvadriraj_broj = lambda x: x**2

print(kvadriraj_broj(2))

#FUNKCIJA MAP

#map(function, iterables)

lista3 = [1,2,3,4]

def kvadriraj2(x):
    return x ** 2

lista_kvadriranih = list(map(kvadriraj2, lista3))

print(lista_kvadriranih)

lista4 = [1,2,3,4,5]

lista_kvadriranih2 = list(map(lambda x : x**2, lista4))

print(lista_kvadriranih2)

studenti = [
     {"ime": "Ivan", "prezime": "Ivić", "jmbag": "0101010101", "godina_rodenja" : 2000},
     {"ime": "Marko", "prezime": "Markić", "jmbag": "0202020202", "godina_rodenja" : 1998},
     {"ime": "Ana", "prezime": "Anić", "jmbag": "0303030303", "godina_rodenja" : 2001},
]

def jmbagovi(studenti):
    jmbagovi = []
    for student in studenti:
        jmbagovi.append(student["jmbag"])
    return jmbagovi

#lista_jmbagova = map(lambda student ...)

print(list(map(lambda x,y : x+y, [1,2,3], [4,5,6])))

#FUNKCIJA FILTER

#filter(function, iterables) - predikat t ili f

lista_filter = [1,2,3,4,5,6,7,8,9,10]

#samo parni staro 
def parni(lista):
     noval =[]
     for element in lista:
         if element % 2 == 0:
            noval.append(element)
     return noval
    

#samo parni
lista_filter2 = list(filter(lambda x: not x%2, lista_filter))

print(lista_filter2)

#filter + lambda

studenti_rodeni_prije_2000 = list(filter(lambda x: x["godina_rodenja"] >= 2000, studenti))

print(studenti_rodeni_prije_2000)

#FUNKCIJE ANY I ALL

print(any([False, False, True])) #True

print(any([False, False, False])) #False

print(all([False, False, True])) #False

print(all([True, True, True])) #True

lista_filter2 = [1,2,3,4,5,6,7,8,9,10]

# nesto krivo: lista_all3 = all(filter(lambda x: not x%2, lista_filter2))
parnost = list(map(lambda broj : broj % 2 == 0, lista_filter2))
print(parnost)
print(all(parnost))

# COMPREHENSION sintaksa

#[expression for element in interable if condition]

#obicno
kvadrati = []

for i in range (1,10):
     kvadrati.append(i ** 2)
    
print(kvadrati)

#map
kvadratimap = list(map(lambda x: x** 2, range(1,11)))
print(kvadratimap)

#comprehension
kvadraticomph = [i**2 for i in range (1,12)]
print(kvadraticomph)

nizovi = ["jabuka","kruska","banana","naranca"]
novi_niz = [len(i) for i in nizovi]
print(novi_niz)
novi_nizskup = {len(i) for i in nizovi}
print(novi_nizskup)

brojevi = [32,24,57,346,76,97,34,86]

parni_comp = [i**2 for i in brojevi if i % 2 == 0]

print(parni_comp)

#ako paran kvadrat, ako neparan kub

paran_neparan = [i**2 if i %2 == 0 else i**3 for i in brojevi]
print(paran_neparan)

#lista imena studenata rodeni prije '99

#list comprehension

imena_rodenih_prije_99 = [studenti["ime"] for studenti in studenti if studenti["godina_rodenja"] < 1999]

print(imena_rodenih_prije_99)

# {key_expression: value_expression for item in iterable if condition}

fruits = ["apple", "banana"]

fruit = {"apple": 2, "banana": 2}

#zadatak napraviti dict sa cmp klkjuc naziv a vrijednost duljina stringa"

fruits_dict = {voce: len(voce) for voce in fruits}

print(fruits_dict)

#najjednostavniji zadaci
#lambda izraz

pomnozi_i_potenciraj = (lambda x,y: (y*5)**x) #DOBIO BOD!

print(pomnozi_i_potenciraj(5,6))

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
    {"ime": "Marko", "prezime": "Marković", "godine": 22},
    {"ime": "Ana", "prezime": "Anić", "godine": 21},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17},
    {"ime": "Mate", "prezime": "Matić", "godine": 18}
]

svi_punoljetni = ...
print(svi_punoljetni) # False



