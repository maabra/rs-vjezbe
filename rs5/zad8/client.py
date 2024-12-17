# Definirajte 2 mikroservisa unutar direktorija cats.

# Prvi mikroservis cat_microservice.py mora slušati na portu 8086 i na endpointu /cats vraćati JSON odgovor s listom činjenica o mačkama. Endpoint /cat mora primati URL parametar amount koji predstavlja broj činjenica koji će se dohvatiti. Na primjer, slanjem zahtjeva na /cat/30 dohvatit će se 30 činjenica o mačkama. Činjenice se moraju dohvaćati konkurentnim slanjem zahtjeva na CatFacts API. Link: https://catfact.ninja/

# Drugi mikroservis cat_fact_check mora slušati na portu 8087 i na endopintu /facts očekivati JSON objekt s listom činjenica o mačkama u tijelu HTTP zahtjeva. Glavna dužnost ovog mikroservisa je da provjeri svaku činjenicu sadrži li riječ cat ili cats, neovisno o velikim i malim slovima. Odgovor neka bude JSON objekt s novom listom činjenica koje zadovoljavaju prethodni uvjet.

# U client.py pozovite ove dvije korutine sekvencijalno, obzirom da drugi mikroservis ovisi o rezultatima prvog. Testirajte kod za proizvoljan broj činjenica.

import asyncio
import aiohttp

async def fetch_data(url, method='GET', data=None):
    async with aiohttp.ClientSession() as session:
        if method == 'GET':
            async with session.get(url) as response:
                return await response.json()
        elif method == 'POST':
            async with session.post(url, json=data) as response:
                return await response.json()

async def main():
    cat_service_url = 'http://localhost:8086/cats?amount=10'
    fact_check_service_url = 'http://localhost:8087/facts'

    # Dohvati činjenice o mačkama
    cat_facts = await fetch_data(cat_service_url)

    # Provjeri činjenice o mačkama
    check_data = {'facts': cat_facts}
    filtered_facts = await fetch_data(fact_check_service_url, method='POST', data=check_data)

    # Ispis rezultata
    print("Činjenice o mačkama:")
    for fact in cat_facts:
        print(fact)

    print("\nFiltrirane činjenice o mačkama:")
    for fact in filtered_facts['filtered_facts']:
        print(fact)

if __name__ == "__main__":
    asyncio.run(main())
