# Definirajte paket shop koji će sadržavati module proizvodi.py i narudzbe.py .
# Modul proizvodi.py :
# definirajte klasu Proizvod s atributima naziv , cijena i dostupna_kolicina . Dodajte metodu ispis
# koja će ispisivati sve atribute proizvoda.
# u listu skladiste pohranite 2 objekta klase Proizvod s proizvoljnim vrijednostima atributa. U ovoj
# listi ćete pohranjivati instance klase Proizvod koje će predstavljati stanje proizvoda u skladištu.
# definirajte funkciju dodaj_proizvod van definicije klase koja će dodavati novi Proizvod u listu
# skladiste .
# U main.py datoteci učitajte modul proizvodi.py iz paketa shop i pozovite pozovite funkciju
# dodaj_proizvod za svaki element iz sljedeće liste:
# proizvodi_za_dodavanje = [
# {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
# {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
# {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
# {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
# ]

# Lista skladiste treba sada sadržavati ukupno 6 elemenata.
# Nakon što to napravite, pozovite metodu ispis za svaki proizvod iz liste skladiste .
# Modul narudzbe.py :
# definirajte klasu Narudzba s atributima: naruceni_proizvodi i ukupna_cijena .
# dodajte funkciju napravi_narudzbu van definicije klase koja prima listu proizvoda kao argument i
# vraća novu instancu klase Narudzba .
# dodajte provjeru u funkciju napravi_narudzbu koja će provjeravati dostupnost proizvoda prije nego
# što se napravi narudžba. Ako proizvoda nema na stanju, ispišite poruku: "Proizvod {naziv} nije
# dostupan!" i ne stvarajte narudžbu.
# dodajte provjere u funkciju napravi_narudzbu koja će provjeriti sljedeća 4 uvjeta:
# argument naruceni_proizvodi mora biti lista
# svaki element u listi mora biti rječni

# svaki rječnik mora sadržavati ključeve naziv , cijena i narucena_kolicina
# lista ne smije biti prazna
# izračunajte ukupnu cijenu narudžbe koju ćete pohraniti u lokalnu varijablu ukupna_cijena u jednoj
# liniji koda.
# narudžbe (instanca klase Narudzba ) pohranite u listu rječnika narudzbe .
# u klasu Narudzba dodajte metodu ispis_narudzbe koja će ispisivati nazive svih naručenih proizvoda,
# količine te ukupnu cijenu narudžbe.
# npr. "Naručeni proizvodi: Laptop x 2, Monitor x 1, Ukupna cijena: 11000 eur".
# U main.py datoteci učitajte modul narudzbe.py iz paketa shop i pozovite funkciju napravi_narudzbu s
# listom proizvoda iz prethodnog zadatka.

# main.py
from shop import proizvodi
from shop import narudzbe

proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

for p in proizvodi_za_dodavanje:
    proizvodi.dodaj_proizvod(p["naziv"], p["cijena"], p["dostupna_kolicina"])

for p in proizvodi.skladiste:
    p.ispis()

naruceni_proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 2},
    {"naziv": "Monitor", "cijena": 1000, "narucena_kolicina": 1}
]

narudzba = narudzbe.napravi_narudzbu(naruceni_proizvodi)
if narudzba:
    narudzba.ispis_narudzbe()
