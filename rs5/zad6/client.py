# Definirajte 2 mikroservisa u 2 različite datoteke. Prvi mikroservis neka sluša na portu 8081 i na endpointu /pozdrav vraća JSON odgovor nakon 3 sekunde čekanja, u formatu: {"message": "Pozdrav nakon 3 sekunde"}. Drugi mikroservis neka sluša na portu 8082 te na istom endpointu vraća JSON odgovor nakon 4 sekunde: {"message": "Pozdrav nakon 4 sekunde"}.

# Unutar client.py datoteke definirajte 1 korutinu koja može slati zahtjev na oba mikroservisa, mora primati argumente url i port. Korutina neka vraća JSON odgovor.

# Korutinu pozovite unutar main korutine. Prvo demonstrirajte sekvencijalno slanje zahtjeva, a zatim konkurentno slanje zahtjeva.

import asyncio
import aiohttp
import time

# Korutina koja šalje zahtjev na mikroservis
async def fetch_data(url, port):
    full_url = f"http://{url}:{port}/pozdrav"
    async with aiohttp.ClientSession() as session:
        async with session.get(full_url) as response:
            return await response.json()

# Main korutina za sekvencijalno i konkurentno slanje zahtjeva
async def main():
    url = "localhost"
    port1 = 8081
    port2 = 8082

    # Sekvencijalno slanje zahtjeva
    start_time = time.time()
    response1 = await fetch_data(url, port1)
    response2 = await fetch_data(url, port2)
    sequential_time = time.time() - start_time

    print("Sekvencijalno slanje zahtjeva:")
    print(response1)
    print(response2)
    print(f"Vrijeme izvršavanja (sekvencijalno): {sequential_time:.2f} sekundi")

    # Konkurentno slanje zahtjeva
    start_time = time.time()
    responses = await asyncio.gather(
        fetch_data(url, port1),
        fetch_data(url, port2)
    )
    concurrent_time = time.time() - start_time

    print("Konkurentno slanje zahtjeva:")
    for response in responses:
        print(response)
    print(f"Vrijeme izvršavanja (konkurentno): {concurrent_time:.2f} sekundi")

# Pokretanje glavne funkcije
if __name__ == "__main__":
    asyncio.run(main())

# Pokretanje mikroservisa

# Pokrenite prvi mikroservis:
# uvicorn server1:app --reload --port 8081

# Pokrenite drugi mikroservis:
# uvicorn server2:app --reload --port 8082

# Pokrenite client.py datoteku kako biste demonstrirali sekvencijalno i konkurentno slanje zahtjeva.
# python client.py