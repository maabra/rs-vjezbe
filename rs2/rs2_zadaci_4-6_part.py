## Zadatak 4: Klase i objekti

# Definirajte klasu Automobil s atributima marka , model , godina_proizvodnje i kilometraža .
# Dodajte metodu ispis koja će ispisivati sve atribute automobila.
# Stvorite objekt klase Automobil s proizvoljnim vrijednostima atributa i pozovite metodu ispis .
# Dodajte novu metodu starost koja će ispisivati koliko je automobil star u godinama, trenutnu
# godine dohvatite pomoću datetime modula.

#import datetime
from datetime import datetime

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis_atributi(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Godina proizvodnje: {self.godina_proizvodnje}")
        print(f"Kilometraža: {self.kilometraza} km")

    def age(self):
        trenutna_godina = datetime.now().year
        starost = trenutna_godina - self.godina_proizvodnje
        print(f"The car is {starost} years old.")

auto1 = Automobil("Renault", "Scenic", 2012, 263000)
auto2 = Automobil("Peugeot", "306", 2000, 424000)

auto1.ispis_atributi()
auto2.ispis_atributi()

auto1.age()
auto1.age()

# 2. Definirajte klasu Kalkulator s atributima a i b . Dodajte metode zbroj , oduzimanje , mnozenje ,
# dijeljenje , potenciranje i korijen koje će izvršavati odgovarajuće operacije nad atributima a i
# b .

class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def zbroj(self):
        return self.a + self.b

    def oduzimanje(self):
        return self.a - self.b

    def mnozenje(self):
        return self.a * self.b

    def dijeljenje(self):
        return self.a / self.b

    def potenciranje(self):
        return self.a ** self.b

    def korijen(self):
        return (self.a ** 0.5, self.b ** 0.5)

a = float(input("Unesite prvi broj, a: "))
b = float(input("Unesite drugi broj, b: "))

kalkulator = Kalkulator(a, b)

print(f"Zbroj: {kalkulator.zbroj()}")
print(f"Oduzimanje: {kalkulator.oduzimanje()}")
print(f"Množenje: {kalkulator.mnozenje()}")
print(f"Dijeljenje: {kalkulator.dijeljenje()}")
print(f"Potenciranje: {kalkulator.potenciranje()}")
print(f"Korijen: {kalkulator.korijen()}")


# 3. Definirajte klasu Student s atributima ime , prezime , godine i ocjene 
# Iterirajte kroz sljedeću listu studenata i za svakog studenta stvorite objekt klase Student i dodajte ga u
# novu listu studenti_objekti :
# studenti = [
# {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
# {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
# {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
# {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
# {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
# {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
# ]
# Dodajte metodu prosjek koja će računati prosječnu ocjenu studenta.
# U varijablu najbolji_student pohranite studenta s najvećim prosjekom ocjena iz liste
# studenti_objekti . Implementirajte u jednoj liniji koda.

class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene
    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]
studenti_objekti = [Student(s["ime"], s["prezime"], s["godine"], s["ocjene"]) for s in studenti]
najbolji_student = max(studenti_objekti, key=lambda s: s.prosjek())
print(najbolji_student.ime, najbolji_student.prezime, najbolji_student.prosjek())
