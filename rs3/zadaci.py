# Definirajte korutinu koja će simulirati dohvaćanje podataka s weba. Podaci neka budu lista
# brojeva od 1 do 10 koju ćete vratiti nakon 3 sekunde. Listu brojeva definirajte comprehensionom.
# Nakon isteka vremena, u korutinu ispišite poruku "Podaci dohvaćeni." i vratite podatke. Riješite bez
# korištenja asyncio.gather() i asyncio.create_task() funkcija.

import asyncio

async def dohvat_podataka():
    await asyncio.sleep(3)
    podaci = [i for i in range(1, 11)]
    print("Podaci dohvaćeni.")
    return podaci

# Pokretanje korutine
async def main():
    podaci = await dohvat_podataka()
    print(podaci)

# Ovo je potreban dio za pokretanje glavne korutine
if __name__ == "__main__":
    asyncio.run(main())

# Definirajte dvije korutine koje će simulirati dohvaćanje podataka s weba. Prva korutina neka vrati
# listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o korisnicima) nakon 3 sekunde, a druga
# korutina neka vrati listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o proizvodima) nakon 5
# sekundi. Korutine pozovite konkurentno korištenjem asyncio.gather() i ispišite rezultate. Program
# se mora izvršavati ~5 sekundi.

import asyncio
import random

async def dohvat_korisnika():
    await asyncio.sleep(3)
    korisnici = [{"id": i, "ime": f"Korisnik{i}"} for i in range(1, 6)]
    print("Podaci o korisnicima dohvaćeni.")
    return korisnici

async def dohvat_proizvoda():
    await asyncio.sleep(5)
    proizvodi = [{"id": i, "naziv": f"Proizvod{i}"} for i in range(1, 6)]
    print("Podaci o proizvodima dohvaćeni.")
    return proizvodi

async def main():
    korisnici, proizvodi = await asyncio.gather(dohvat_korisnika(), dohvat_proizvoda())
    print("Rezultati dohvaćanja:")
    print("Korisnici:", korisnici)
    print("Proizvodi:", proizvodi)

# Ovo je potreban dio za pokretanje glavne korutine
if __name__ == "__main__":
    asyncio.run(main())


# Definirajte korutinu autentifikacija() koja će simulirati autentifikaciju korisnika na
# poslužiteljskoj strani. Korutina kao ulazni parametar prima rječnik koji opisuje korisnika, a sastoji se
# od ključeva korisnicko_ime , email i lozinka . Unutar korutine simulirajte provjeru korisničkog
# imena na način da ćete provjeriti nalaze li se par korisnicko_ime i email u bazi korisnika. Ova
# provjera traje 3 sekunde.

# Ako se korisnik ne nalazi u bazi, vratite poruku "Korisnik {korisnik} nije pronađen."
# Ako se korisnik nalazi u bazi, potrebno je pozvati vanjsku korutinu autorizacija() koja će simulirati
# autorizaciju korisnika u trajanju od 2 sekunde. Funkcija kao ulazni parametar prima rječnik korisnika iz baze
# i lozinku proslijeđenu iz korutine autentifikacija() . Autorizacija simulira dekripciju lozinke (samo
# provjerite podudaranje stringova) i provjeru s lozinkom iz baze_lozinka. Ako su lozinke jednake, korutine
# vraća poruku "Korisnik {korisnik}: Autorizacija uspješna." , a u suprotnom "Korisnik
# {korisnik}: Autorizacija neuspješna." .

# Korutinu autentifikacija() pozovite u main() funkciji s proizvoljnim korisnikom i lozinkom.

import asyncio

# Simulirana baza korisnika
baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

# Simulirana baza lozinki
baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autorizacija(korisnik, unesena_lozinka):
    await asyncio.sleep(2)  # Simulacija trajanja autorizacije
    if korisnik['lozinka'] == unesena_lozinka:
        return f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija uspješna."
    else:
        return f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija neuspješna."

async def autentifikacija(korisnik_info):
    await asyncio.sleep(3)  # Simulacija trajanja provjere korisničkog imena i emaila
    korisnicko_ime = korisnik_info.get('korisnicko_ime')
    email = korisnik_info.get('email')
    
    korisnik = next((k for k in baza_korisnika if k['korisnicko_ime'] == korisnicko_ime and k['email'] == email), None)
    
    if korisnik:
        lozinka_info = next((l for l in baza_lozinka if l['korisnicko_ime'] == korisnicko_ime), None)
        if lozinka_info:
            poruka = await autorizacija(lozinka_info, korisnik_info.get('lozinka'))
            return poruka
    return f"Korisnik {korisnicko_ime} nije pronađen."

# Glavna funkcija za pokretanje autentifikacije
async def main():
    korisnik_info = {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com', 'lozinka': 'lozinka123'}
    rezultat = await autentifikacija(korisnik_info)
    print(rezultat)

# Pokretanje glavne funkcije
if __name__ == "__main__":
    asyncio.run(main())


# Definirajte korutinu provjeri_parnost koja će simulirati "super zahtjevnu operaciju" provjere
# parnosti broja putem vanjskog API-ja. Korutina prima kao argument broj za koji treba provjeriti
# parnost, a vraća poruku "Broj {broj} je paran." ili "Broj {broj} je neparan." nakon 2 sekunde.
# Unutar main funkcije definirajte listu 10 nasumičnih brojeva u rasponu od 1 do 100 (koristite random
# modul). Listu brojeva izgradite kroz list comprehension sintaksu. Nakon toga, pohranite u listu zadaci
# 10 Task objekata koji će izvršavati korutinu provjeri_parnost za svaki broj iz liste (također kroz list
# comprehension). Na kraju, koristeći asyncio.gather() , pokrenite sve korutine konkurentno i ispišite
# rezultate.

import asyncio
import random

async def provjeri_parnost(broj):
    await asyncio.sleep(2)  # Simulacija trajanja vanjske provjere
    if broj % 2 == 0:
        return f"Broj {broj} je paran."
    else:
        return f"Broj {broj} je neparan."

async def main():
    # Definiranje liste 10 nasumičnih brojeva u rasponu od 1 do 100
    brojevi = [random.randint(1, 100) for _ in range(10)]
    print(f"Generirani brojevi: {brojevi}")

    # Kreiranje liste zadataka za provjeru parnosti svakog broja
    zadaci = [provjeri_parnost(broj) for broj in brojevi]

    # Pokretanje svih korutina paralelno i ispis rezultata
    rezultati = await asyncio.gather(*zadaci)
    for rezultat in rezultati:
        print(rezultat)

# Pokretanje glavne funkcije
if __name__ == "__main__":
    asyncio.run(main())


# Definirajte korutinu secure_data koja će simulirati enkripciju osjetljivih podataka. Kako se u
# praksi enkripcija radi na poslužiteljskoj strani, korutina će simulirati enkripciju podataka u trajanju od 3
# sekunde. Korutina prima kao argument rječnik osjetljivih podataka koji se sastoji od ključeva prezime ,
# broj_kartice i CVV . Definirajte listu s 3 rječnika osjetljivih podataka. Pohranite u listu zadaci kao u
# prethodnom zadatku te pozovite zadatke koristeći asyncio.gather() . Korutina secure_data mora za
# svaki rječnik vratiti novi rječnik u obliku: {'prezime': prezime , 'broj_kartice': 'enkriptirano',
# 'CVV': 'enkriptirano'} . Za fake enkripciju koristite funkciju hash(str) koja samo vraća hash
# vrijednost ulaznog stringa.

import asyncio

# Korutina koja simulira enkripciju osjetljivih podataka
async def secure_data(podaci):
    await asyncio.sleep(3)  # Simulacija trajanja enkripcije
    enkriptirani_podaci = {
        'prezime': podaci['prezime'],
        'broj_kartice': hash(podaci['broj_kartice']),
        'CVV': hash(podaci['CVV'])
    }
    return enkriptirani_podaci

# Glavna funkcija za pokretanje enkripcije
async def main():
    # Definiranje liste s tri rječnika osjetljivih podataka
    osjetljivi_podaci = [
        {'prezime': 'Novak', 'broj_kartice': '1234567812345678', 'CVV': '123'},
        {'prezime': 'Ivić', 'broj_kartice': '8765432187654321', 'CVV': '321'},
        {'prezime': 'Horvat', 'broj_kartice': '1122334455667788', 'CVV': '456'}
    ]

    # Kreiranje liste zadataka za enkripciju svakog rječnika osjetljivih podataka
    zadaci = [secure_data(podaci) for podaci in osjetljivi_podaci]

    # Pokretanje svih korutina paralelno i ispis rezultata
    enkriptirani_rezultati = await asyncio.gather(*zadaci)
    for rezultat in enkriptirani_rezultati:
        print(rezultat)

# Pokretanje glavne funkcije
if __name__ == "__main__":
    asyncio.run(main())
