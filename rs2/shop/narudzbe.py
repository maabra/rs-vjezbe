# narudzbe.py
class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        proizvodi_info = ", ".join([f"{p['naziv']} x {p['narucena_kolicina']}" for p in self.naruceni_proizvodi])
        print(f"Naručeni proizvodi: {proizvodi_info}, Ukupna cijena: {self.ukupna_cijena} eur")

def napravi_narudzbu(naruceni_proizvodi):
    if not isinstance(naruceni_proizvodi, list) or not naruceni_proizvodi:
        print("Neispravan unos narudžbe.")
        return None
    for item in naruceni_proizvodi:
        if not all(key in item for key in ['naziv', 'cijena', 'narucena_kolicina']):
            print("Neispravan unos narudžbe.")
            return None
    
    ukupna_cijena = sum(p['cijena'] * p['narucena_kolicina'] for p in naruceni_proizvodi)
    return Narudzba(naruceni_proizvodi, ukupna_cijena)
