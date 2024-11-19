## Zadatak 1: Lambda izrazi
# Napišite korespondirajuće lambda izraze za sljedeće funkcije:

# 1. Kvadriranje broja:

# def kvadriraj(x):
# return x ** 2

kvadriraj = lambda x: x ** 2

# 2. Zbroji pa kvadriraj:

# def zbroji_pa_kvadriraj(a, b):
# return (a + b) ** 2

zbroji_pa_kvadriraj = lambda a, b: (a + b) ** 2

# 3. Kvadriraj duljinu niza:

# def kvadriraj_duljinu(niz):
# return len(niz) ** 2

kvadriraj_duljinu = lambda niz: len(niz) ** 2

# 4. Pomnoži vrijednost s 5 pa potenciraj na x:

# def pomnozi_i_potenciraj(x, y):
# return (y * 5) ** x

pomnozi_i_potenciraj = lambda x, y: (y * 5) ** x

# 5. Vrati True ako je broj paran, inače vrati None:

# def paran_broj(x):
# if x % 2 == 0:
# return True
# else:
# return None

paran_broj = lambda x: True if x % 2 == 0 else None

## Zadatak 2: Funkcije višeg reda
# Definirajte sljedeće izraze korištenjem funkcija višeg reda i lambda izraza:

# 1. Koristeći funkciju map , kvadrirajte duljine svih nizova u listi:

# nizovi = ["jabuka", "kruška", "banana", "naranča"]
# kvadrirane_duljine = ...
# print(kvadrirane_duljine) # [36, 36, 36, 49]


nizovi = ["jabuka", "kruška", "banana", "naranča"]
kvadrirane_duljine = list(map(lambda x: len(x) ** 2, nizovi))
print(kvadrirane_duljine) # Doći će nam traženo

# 2. Koristeći funkciju filter , filtrirajte samo brojeve koji su veći od 5:

# brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]
# veci_od_5 = ...
# print(veci_od_5) # [21, 33, 45, 9, 10]

brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]
veci_od_5 = list(filter(lambda x: x > 5, brojevi))
print(veci_od_5) # Doći će nam traženo

# 3. Koristeći odgovarajuću funkciju višeg reda i lambda izraz (bez comprehensiona), pohranite u varijablu
# transform rezultat kvadriranja svih brojeva u listi gdje rezultat mora biti rječnik gdje su ključevi
# originalni brojevi, a vrijednosti kvadrati tih brojeva:

# brojevi = [10, 5, 12, 15, 20]
# transform = ...
# print(transform) # {10: 100, 5: 25, 12: 144, 15: 225, 20: 400}

brojevi = [10, 5, 12, 15, 20]
transform = {x: x ** 2 for x in brojevi}
print(transform) # {10: 100, 5: 25, 12: 144, 15: 225, 20: 400}

#4. Koristeći funkcije all i map , provjerite jesu li svi studenti punoljetni:

# studenti = [
# {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
# {"ime": "Marko", "prezime": "Marković", "godine": 22},
# {"ime": "Ana", "prezime": "Anić", "godine": 21},
# {"ime": "Petra", "prezime": "Petrić", "godine": 13},
# {"ime": "Iva", "prezime": "Ivić", "godine": 17},
# {"ime": "Mate", "prezime": "Matić", "godine": 18}
# ]
# svi_punoljetni = ...
# print(svi_punoljetni) # False

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
    {"ime": "Marko", "prezime": "Marković", "godine": 22},
    {"ime": "Ana", "prezime": "Anić", "godine": 21},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17},
    {"ime": "Mate", "prezime": "Matić", "godine": 18}
]

svi_punoljetni = all(student["godine"] >= 18 for student in studenti)
print(svi_punoljetni)  # Doći će nam traženo, False

# 5. Definirajte varijablu min_duljina koja će pohranjivati int . Koristeći odgovarajuću funkciju višeg reda
# i lambda izraz, pohranite u varijablu duge_rijeci sve riječi iz liste rijeci koje su dulje od
# min_duljina :

# rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
# "pjesma", "otorinolaringolog"]
# min_duljina = prompt("Unesite minimalnu duljinu riječi: ")
# # min_duljina = 7
# duge_rijeci = ...
# # print(duge_rijeci) # ['zvijezda', 'prijatelj', 'čokolada', 'otorinolaringolog']

rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"]
min_duljina = int(input("Unesite minimalnu duljinu riječi: "))  # Replace prompt with input for Python script

duge_rijeci = list(filter(lambda x: len(x) >= min_duljina, rijeci))
print(duge_rijeci)  # Doći će nam traženo, ['zvijezda', 'prijatelj', 'čokolada', 'otorinolaringolog']

## Zadatak 3: Comprehension sintaksa

# 1. Koristeći list comprehension, izgradite listu parnih kvadrata brojeva od 20 do 50:

# parni_kvadrati = ...
# print(parni_kvadrati) # [400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764,
# 1936, 2116, 2304, 2500]

#parni_kvadrati = [x**2 for x in range(20, 50) if x % 2 == 0]
parni_kvadrati = [x**2 for x in range(20, 51) if x % 2 == 0]
print(parni_kvadrati) # Doći će nam traženo

# 2. Koristeći list comprehension, izgradite listu duljina svih nizova u listi rijeci , ali samo za nizove koji
# sadrže slovo a :

# rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
# "pjesma", "otorinolaringolog"]
# duljine_sa_slovom_a = ...
# print(duljine_sa_slovom_a) # [6, 3, 6, 8, 9, 8, 6, 17]

rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"]

duljine_sa_slovom_a = [len(rijec) for rijec in rijeci if 'a' in rijec]
print(duljine_sa_slovom_a)  # Doći će nam traženo

# 3. Koristeći list comprehension, izgradite listu rječnika gdje su ključevi brojevi od 1 do 10, a vrijednosti
# kubovi tih brojeva, ali samo za neparne brojeve, za parne brojeve neka vrijednost bude sam broj:

# kubovi = ...
# print(kubovi) # [{1: 1}, {2: 2}, {3: 27}, {4: 4}, {5: 125}, {6: 6}, {7: 343}, {8: 8}, {9:
# 729}, {10: 10}]

#kubovi = [{x: x ** 3} for x in range(1, 10)]
kubovi = [{x: x ** 3} for x in range(1, 11)]
print(kubovi)  # [{1: 1}, {2: 8}, {3: 27}, {4: 64}, {5: 125}, {6: 216}, {7: 343}, {8: 512}, {9: 729}, {10: 1000}]

