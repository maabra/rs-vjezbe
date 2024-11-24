# proizvodi.py
class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        print(f"Naziv: {self.naziv}, Cijena: {self.cijena}, Dostupna količina: {self.dostupna_kolicina}")

skladiste = [
    Proizvod("Proizvod1", 100, 5),
    Proizvod("Proizvod2", 200, 3)
]

def dodaj_proizvod(naziv, cijena, dostupna_kolicina):
    skladiste.append(Proizvod(naziv, cijena, dostupna_kolicina))
