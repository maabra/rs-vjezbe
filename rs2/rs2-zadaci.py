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
