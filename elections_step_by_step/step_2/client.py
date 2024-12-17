# elections/client.py

import aiohttp
import asyncio

# Funkcija za simulaciju glasanja
async def glasaj_klijent(opcija):
    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost:8080/glasaj', json={"opcija": opcija}) as response:
            return await response.json()

# Funkcija za simulaciju prikaza rezultata
async def rezultati_klijent():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:8080/rezultati') as response:
            return await response.json()

# Testiranje poslužitelja
async def main():
    print("Glasanje za 'plavi':")
    result = await glasaj_klijent('plavi')
    print(result)
    
    print("Glasanje za 'crveni':")
    result = await glasaj_klijent('crveni')
    print(result)
    
    print("Glasanje za 'nepoznata opcija':")
    result = await glasaj_klijent('zeleni')
    print(result)
    
    print("Trenutni rezultati:")
    rezultati = await rezultati_klijent()
    print(rezultati)

if __name__ == '__main__':
    asyncio.run(main())
