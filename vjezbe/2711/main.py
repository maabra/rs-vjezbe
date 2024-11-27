# kolokvij simulacija slanja zahtjeva, sekvenijalno ili konkurentno

# aiohttp pomocu posluzitelja

import asyncio
import aiohttp

# async def fetch_fact(session):
#     print("Šaljem zahtjev...")
#     rezultat = await session.get("https://catfact.ninja/fact")
#     return (await rezultat.json)
# async def main():
#     async with aiohttp.ClientSession() as session:
#         response = await session.get("https://catfact.ninja/fact")
#         print(response.status) # 200
#         print ("Deserijalizacija JSONa:", await response.json())


asyncio.run(main())

