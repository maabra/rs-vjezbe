# Definirajte 3 mikroservisa unutar direktorija microservice_calculations. Prvi mikroservis neka sluša na portu 8083 i na endpointu /zbroj vraća JSON bez čekanja. Ulazni podatak u tijelu zahtjeva neka bude lista brojeva, a odgovor neka bude zbroj svih brojeva. Dodajte provjeru ako brojevi nisu proslijeđeni, vratite odgovarajući HTTP odgovor i statusni kod.

# Drugi mikroservis neka sluša na portu 8084 te kao ulazni podataka prima iste podatke. Na endpointu /umnozak neka vraća JSON odgovor s umnoškom svih brojeva. Dodajte provjeru ako brojevi nisu proslijeđeni, vratite odgovarajući HTTP odgovor i statusni kod.

# Treći mikroservis pozovite nakon konkurentnog izvršavanja prvog i drugog mikroservisa. Dakle treći ide sekvencijalno jer mora čekati rezultati prethodna 2. Ovaj mikroservis neka sluša na portu 8085 te na endpointu /kolicnik očekuje JSON s podacima prva dva servisa. Kao odgovor mora vratiti količnik umnoška i zbroja. Dodajte provjeru i vratite odgovarajući statusni kod ako se pokuša umnožak dijeliti s 0.

# U client.py pozovite konkurentno s proizvoljnim podacima prva dva mikroservisa, a zatim sekvencijalno pozovite treći mikroservis.

import asyncio
import aiohttp

async def fetch_data(url, port, endpoint, data):
    full_url = f"http://{url}:{port}{endpoint}"
    async with aiohttp.ClientSession() as session:
        async with session.post(full_url, json=data) as response:
            return await response.json()

async def main():
    url = "localhost"
    port1 = 8083
    port2 = 8084
    port3 = 8085
    data = {'brojevi': [1, 2, 3, 4, 5]}
    
    # Konkurentno slanje zahtjeva prvom i drugom mikroservisu
    responses = await asyncio.gather(
        fetch_data(url, port1, '/zbroj', data),
        fetch_data(url, port2, '/umnozak', data)
    )

    zbroj = responses[0].get('zbroj')
    umnozak = responses[1].get('umnozak')
    
    if zbroj is not None and umnozak is not None:
        # Sekvencijalno slanje zahtjeva trećem mikroservisu
        result = await fetch_data(url, port3, '/kolicnik', {'zbroj': zbroj, 'umnozak': umnozak})
        print(result)
    else:
        print("Greška u dobivanju zbroja ili umnoška.")

if __name__ == "__main__":
    asyncio.run(main())
