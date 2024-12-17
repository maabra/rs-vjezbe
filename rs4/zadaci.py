# Definirajte korutinu fetch_users koja će slati GET zahtjev na JSONPlaceholder API na URL-u:
# https://jsonplaceholder.typicode.com/users . Morate simulirate slanje 5 zahtjeva konkurentno
# unutar main korutine. Unutar main korutine izmjerite vrijeme izvođenja programa, a rezultate
# pohranite u listu odjedanput koristeći asyncio.gather funkciju. Nakon toga koristeći map funkcije ili
# list comprehension izdvojite u zasebne 3 liste: samo imena korisnika, samo email adrese korisnika i
# samo username korisnika. Na kraju main korutine ispišite sve 3 liste i vrijeme izvođenja programa.

import asyncio
import aiohttp
import time

async def fetch_users(session):
    url = "https://jsonplaceholder.typicode.com/users"
    async with session.get(url) as response:
        return await response.json()

async def main():
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        # Kreirajte listu zadataka za konkurentno slanje 5 zahtjeva
        tasks = [fetch_users(session) for _ in range(5)]
        
        # Koristite asyncio.gather za pokretanje svih korutina paralelno
        results = await asyncio.gather(*tasks)
        
        # Pohranjivanje rezultata u jedinstvenu listu
        all_users = [user for result in results for user in result]

        # Izdvajanje imena, email adresa i korisničkih imena
        imena = [user['name'] for user in all_users]
        emailovi = [user['email'] for user in all_users]
        korisnicka_imena = [user['username'] for user in all_users]

        # Ispis rezultata i vrijeme izvođenja
        print("Imena korisnika:", imena)
        print("Email adrese korisnika:", emailovi)
        print("Korisnicka imena:", korisnicka_imena)
    
    end_time = time.time()
    print(f"Vrijeme izvođenja: {end_time - start_time:.2f} sekundi")

if __name__ == "__main__":
    asyncio.run(main())
# U ovom kodu:

#     Definiramo korutinu fetch_users() koja koristi aiohttp za slanje GET zahtjeva na JSONPlaceholder API.

#     Unutar glavne funkcije main() mjerimo vrijeme izvođenja programa pomoću time.time().

#     Kreiramo aiohttp.ClientSession() za upravljanje HTTP vezom.

#     Kreiramo listu zadataka gdje svaka korutina fetch_users() šalje zahtjev i koristimo asyncio.gather() za konkurentno pokretanje svih zadataka.

#     Pohranjujemo sve korisnike u jednu listu, a zatim pomoću list comprehension izdvajamo imena, email adrese i korisnička imena.

#     Ispisujemo rezultate i vrijeme izvođenja programa.




# Definirajte dvije korutine, od kojih će jedna služiti za dohvaćanje činjenica o mačkama koristeći
# get_cat_fact korutinu koja šalje GET zahtjev na URL: https://catfact.ninja/fact . Izradite 20
# Task objekata za dohvaćanje činjenica o mačkama te ih pozovite unutar main korutine i rezultate
# pohranite odjednom koristeći asyncio.gather funkciju. Druga korutina filter_cat_facts ne šalje
# HTTP zahtjeve, već mora primiti gotovu listu činjenica o mačkama i vratiti novu listu koja sadrži samo
# one činjenice koje sadrže riječ "cat" ili "cats" (neovisno o velikim/malim slovima).

import asyncio
import aiohttp

# Korutina koja dohvaća činjenice o mačkama
async def get_cat_fact(session):
    url = "https://catfact.ninja/fact"
    async with session.get(url) as response:
        data = await response.json()
        return data['fact']

# Korutina koja filtrira činjenice o mačkama koje sadrže riječ "cat" ili "cats"
async def filter_cat_facts(facts):
    filtered_facts = [fact for fact in facts if "cat" in fact.lower() or "cats" in fact.lower()]
    return filtered_facts

# Glavna funkcija za dohvaćanje i filtriranje činjenica o mačkama
async def main():
    async with aiohttp.ClientSession() as session:
        # Kreiranje 20 Task objekata za dohvaćanje činjenica o mačkama
        tasks = [get_cat_fact(session) for _ in range(20)]
        
        # Dohvaćanje svih činjenica odjednom
        cat_facts = await asyncio.gather(*tasks)
        
        # Ispisivanje svih dohvaćenih činjenica
        print("Sve činjenice o mačkama:")
        for fact in cat_facts:
            print(fact)
        
        # Filtriranje činjenica
        filtered_facts = await filter_cat_facts(cat_facts)
        
        # Ispisivanje filtriranih činjenica
        print("\nFiltrirane činjenice o mačkama:")
        for fact in filtered_facts:
            print(fact)

# Pokretanje glavne funkcije
if __name__ == "__main__":
    asyncio.run(main())

# U ovom kodu:

#     Korutina get_cat_fact() šalje GET zahtjev na URL https://catfact.ninja/fact i vraća činjenicu o mačkama.

#     Korutina filter_cat_facts() prima listu činjenica i vraća novu listu koja sadrži samo one činjenice koje sadrže riječ "cat" ili "cats" (neovisno o velikim/malim slovima).

#     Unutar glavne funkcije main() kreiramo 20 Task objekata za dohvaćanje činjenica o mačkama koristeći asyncio.gather() za paralelno izvršavanje.

#     Nakon dohvaćanja svih činjenica, ispisujemo ih.

#     Filtriramo činjenice koje sadrže riječ "cat" ili "cats" i ispisujemo filtrirane činjenice.    





# Korutina get_dog_fact neka dohvaća činjenicu o psima na URL-u: https://dogapi.dog/api/v2/facts .
# Nakon toga, definirajte korutinu get_cat_fact koja dohvaća činjenicu o mačkama slanjem zahtjeva na
# URL: https://catfact.ninja/fact .
# Istovremeno pohranite rezultate izvršavanja ovih Taskova koristeći asyncio.gather(*dog_facts_tasks,
# *cat_facts_tasks) funkciju u listu dog_cat_facts , a zatim ih koristeći list slicing odvojite u dvije liste
# obzirom da znate da je prvih 5 činjenica o psima, a drugih 5 o mačkama.
# Na kraju, definirajte i treću korutinu mix_facts koja prima liste dog_facts i cat_facts i vraća novu
# listu koja za vrijednost indeksa i sadrži činjenicu o psima ako je duljina činjenice o psima veća od duljine
# činjenice o mačkama na istom indeksu, inače vraća činjenicu o mački. Na kraju ispišite rezultate filtriranog
# niza činjenica. Liste možete paralelno iterirati koristeći zip funkciju, npr. for dog_fact, cat_fact in
# zip(dog_facts, cat_facts) .

import asyncio
import aiohttp

# Korutina za dohvaćanje činjenica o psima
async def get_dog_fact(session):
    url = "https://dogapi.dog/api/v2/facts"
    async with session.get(url) as response:
        data = await response.json()
        return data['facts'][0]['text']

# Korutina za dohvaćanje činjenica o mačkama
async def get_cat_fact(session):
    url = "https://catfact.ninja/fact"
    async with session.get(url) as response:
        data = await response.json()
        return data['fact']

# Korutina za miješanje činjenica
async def mix_facts(dog_facts, cat_facts):
    mixed_facts = [dog_fact if len(dog_fact) > len(cat_fact) else cat_fact
                   for dog_fact, cat_fact in zip(dog_facts, cat_facts)]
    return mixed_facts

# Glavna funkcija za dohvaćanje i miješanje činjenica
async def main():
    async with aiohttp.ClientSession() as session:
        # Kreiranje Task objekata za dohvaćanje činjenica o psima i mačkama
        dog_facts_tasks = [get_dog_fact(session) for _ in range(5)]
        cat_facts_tasks = [get_cat_fact(session) for _ in range(5)]
        
        # Dohvaćanje svih činjenica odjednom
        dog_cat_facts = await asyncio.gather(*dog_facts_tasks, *cat_facts_tasks)
        
        # Razdvajanje činjenica o psima i mačkama
        dog_facts = dog_cat_facts[:5]
        cat_facts = dog_cat_facts[5:]
        
        # Ispisivanje svih dohvaćenih činjenica
        print("Činjenice o psima:")
        for fact in dog_facts:
            print(fact)
        
        print("\nČinjenice o mačkama:")
        for fact in cat_facts:
            print(fact)

        # Miješanje činjenica i ispis rezultata
        mixed_facts = await mix_facts(dog_facts, cat_facts)
        print("\nPomiješane činjenice:")
        for fact in mixed_facts:
            print(fact)

# Pokretanje glavne funkcije
if __name__ == "__main__":
    asyncio.run(main())

# U ovom kodu:

#     Korutina get_dog_fact() dohvaća činjenicu o psima sa URL-a https://dogapi.dog/api/v2/facts.

#     Korutina get_cat_fact() dohvaća činjenicu o mačkama sa URL-a https://catfact.ninja/fact.

#     Korutina mix_facts() prima liste činjenica o psima i mačkama te vraća novu listu koja za svaki indeks i sadrži činjenicu o psima ako je duljina činjenice o psima veća od duljine činjenice o mačkama na istom indeksu, inače vraća činjenicu o mački.

#     Unutar glavne funkcije main() kreiramo Task objekte za dohvaćanje činjenica o psima i mačkama, koristimo asyncio.gather() za paralelno izvršavanje, razdvajamo rezultate u dvije liste i zatim koristimo korutinu mix_facts() za miješanje činjenica.
