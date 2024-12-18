import aiohttp
import asyncio
import random

# Funkcija za simulaciju glasanja klijenta
async def glasaj_klijent(session, opcija):
    async with session.post('http://localhost:8080/glasaj', json={"opcija": opcija}) as response:
        result = await response.json()
        return result

# Funkcija za simulaciju slanja velikog broja glasova
async def mirage_simulation(broj_zahtjeva=500):
    opcije = ['plavi', 'crveni']
    uspjesni_zahtjevi = 0
    neuspjesni_zahtjevi = 0

    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(broj_zahtjeva):
            opcija = random.choice(opcije)
            tasks.append(glasaj_klijent(session, opcija))

        responses = await asyncio.gather(*tasks, return_exceptions=True)
        
        for response in responses:
            if isinstance(response, dict) and response.get('status') == 'uspješno glasanje':
                uspjesni_zahtjevi += 1
            else:
                neuspjesni_zahtjevi += 1

    print(f"Uspješni zahtjevi: {uspjesni_zahtjevi}")
    print(f"Neuspješni zahtjevi: {neuspjesni_zahtjevi}")

# Testiranje funkcije
async def main():
    await mirage_simulation(500)

if __name__ == '__main__':
    asyncio.run(main())
