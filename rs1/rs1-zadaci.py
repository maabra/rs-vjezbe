'''
Vj 7
Napišite program koji traži od korisnika da unese lozinku. Lozinka mora zadovoljavati sljedeće uvjete:
1. ako duljina lozinke nije između 8 i 15 znakova, ispišite poruku "Lozinka mora sadržavati između 8 i 15
znakova".
2. ako lozinka ne sadrži barem jedno veliko slovo i jedan broj, ispišite "Lozinka mora sadržavati barem
jedno veliko slovo i jedan broj"
3. ako lozinka sadrži riječ "password" ili "lozinka" (bez obzira na velika i mala slova), ispišite: "Lozinka
ne smije sadržavati riječi 'password' ili 'lozinka'"
4. ako lozinka zadovoljava sve uvjete, ispišite "Lozinka je jaka!"
Metode za normalizaciju stringova: lower() , upper() , islower() , isupper() .
Provjera je li znakovni niz broj: isdigit()
Kod za provjeru dodajte u funkciju provjera_lozinke(lozinka).
'''
def provjera_lozinke(lozinka):
    # Provjera duljine lozinke
    if len(lozinka) < 8 or len(lozinka) > 15:
        return "Lozinka mora sadržavati između 8 i 15 znakova."
    ima_veliko_slovo = any(char.isupper() for char in lozinka)
    ima_broj = any(char.isdigit() for char in lozinka)
    if not ima_veliko_slovo or not ima_broj:
        return "Lozinka mora sadržavati barem jedno veliko slovo i jedan broj."
    if "password" in lozinka.lower() or "lozinka" in lozinka.lower():
        return "Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'."
    return "Lozinka je jaka!"

unesena_lozinka = input("Unesite lozinku: ")
rezultat = provjera_lozinke(unesena_lozinka)
print(rezultat)

'''
Vj 8
Napišite funkciju koja prima listu cijelih brojeva i vraća novu lista koja sadrži samo parne brojeve iz
originalne liste.
Primjer:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filtriraj_parne(lista)) # [2, 4, 6, 8, 10]
'''
def unos_liste():
    lista = input("Unesite listu brojeva i odvojite ih razmakom: ")
    lista_brojeva = list(map(int, lista.split()))
    return lista_brojeva
def filtrirani(lista):
    return [broj for broj in lista if broj % 2 == 0]
lista = unos_liste()
filtrirani_brojevi = filtrirani(lista)
print(f"Samo parni brojevi: {filtrirani_brojevi}")

'''
Vježba 9: Uklanjanje duplikata iz liste
Napišite funkciju koja prima listu i vraća novu listu koja ne sadrži duplikate. Implementaciju odradite
pomoćnim skupom.
Primjer:
lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(ukloni_duplikate(lista)) # [1, 2, 3, 4, 5]
'''
def ukloni_duplikate(lista):
    return list(set(lista2))
unos = input("Unesite elemente liste s duplikatimai odvojite ih zarezom: ")
lista2 = [int(x.strip()) for x in unos.split(",")]
print("Lista bez duplikata:", ukloni_duplikate(lista2))


'''
Vježba 10: Brojanje riječi u tekstu
Napišite funkciju koja broji koliko se puta svaka riječ pojavljuje u tekstu i vraća rječnik s rezultatima.
Primjer:
tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je
vrlo popularan."
print(brojanje_riječi(tekst))
# {'Python': 2, 'je': 3, 'programski': 1, 'jezik': 1, 'koji': 1, 'jednostavan': 1, 'za':
1, 'učenje': 1, 'i': 1, 'korištenje.': 1, 'vrlo': 1, 'popularan.': 1}

'''
def brojanje(tekst):
    riječi = tekst.split()
    brojač = {}
    for riječ in riječi:
        if riječ in brojač:
            brojač[riječ] += 1
        else:
            brojač[riječ] = 1
    return brojač
unos2 = input("Unesite tekst: ")
print("Riječi u tekstu su:", brojanje(unos2))

'''
Vježba 11: Grupiranje elemenata po paritetu
Napišite funkciju koja prima listu brojeva i vraća rječnik s dvije liste: jedna za parne brojeve, a druga za
neparne brojeve.
Primjer:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(grupiraj_po_paritetu(lista))
# {'parni': [2, 4, 6, 8, 10], 'neparni': [1, 3, 5, 7, 9]}
'''
def grupiraj_po_paritetu(lista):
    rezultat = {'parni': [], 'neparni': []}
    for broj in lista:
        if broj % 2 == 0:
            rezultat['parni'].append(broj) 
        else:
            rezultat['neparni'].append(broj) 
    return rezultat

def unos_liste():
    unos = input("Unesite brojeve odvojene zarezom ali zajedno: ")
    lista = [int(broj.strip()) for broj in unos.split(',')]
    return lista

lista = unos_liste()
print(grupiraj_po_paritetu(lista))

'''
Vj 12
Napišite funkciju koja prima rječnik i vraća novi rječnik u kojem su ključevi i vrijednosti zamijenjeni.
Primjer:rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
print(obrni_rjecnik(rjecnik))
# {'Ivan': 'ime', 'Ivić': 'prezime', 25: 'dob'}
'''
def obrnuti_rjecnik(rjecnik):
    obrnut_rjecnik = {}
    for kljuc, vrijednost in rjecnik.items():
        obrnut_rjecnik[vrijednost] = kljuc
    return obrnut_rjecnik
def unos_rjecnika():
    rjecnik = {}
    while True:
        kljuc = input("Unesite ključ (ili samo Enter za kraj unosa u riječnik): ")
        if kljuc == "":
            break
        vrijednost = input("Unesite vrijednost za ključ '{}': ".format(kljuc))
        rjecnik[kljuc] = vrijednost
    return rjecnik
rjecnik = unos_rjecnika() 
print("Originalni rječnik:", rjecnik)
print("Obrnuti rječnik:", obrnuti_rjecnik(rjecnik))
