import aiohttp
import asyncio

async def fetch_service_1(brojevi):
  async with aiohttp.ClientSession() as session:
    podatak_koji_saljemo = {"brojevi": brojevi}
    rezultat = await session.post('http://localhost:8081/zbroj', json=podatak_koji_saljemo)
    return await rezultat.json()


async def fetch_service_2(brojevi, zbroj):
  async with aiohttp.ClientSession() as session:
    podatak_koji_saljemo = {"brojevi": brojevi}
    microservice_ratio_result = await session.post('http://localhost:8082/ratio', json={"podaci": podatak_koji_saljemo, "zbroj": zbroj})
    microservice_ratio_data = await microservice_ratio_result.json() # podaci iz odgovora 2. mikroservisa
    return await microservice_ratio_data.json()

async def main():
    print("Pokrećem main korutinu")
    brojevi = [i for i in range (1, 11)]
    print(brojevi)

    zbroj = await fetch_service_1(brojevi)

asyncio.run(main())

'''

async def main():
  print("Pokrećem main korutinu")
  data = [i for i in range (1, 11)]
  data_json = {"podaci": data}
  async with aiohttp.ClientSession() as session:
    # slanje zahtjeva na 1. mikroservis
    microservice_sum_result = await session.post('http://localhost:8081/zbroj', json=data_json)
    microservice_sum_data = await microservice_sum_result.json() # podaci iz odgovora 1. mikroservisa
    zbroj = microservice_sum_data.get("zbroj")

    # slanje zahtjeva na 2. mikroservis
    microservice_ratio_result = await session.post('http://localhost:8082/ratio', json={"podaci": data, "zbroj": zbroj})
    microservice_ratio_data = await microservice_ratio_result.json() # podaci iz odgovora 2. mikroservisa
    ratio_list = microservice_ratio_data.get("ratio_list")

    print(f"Zbroj: {zbroj}")
    print(f"Lista omjera: {ratio_list}")

asyncio.run(main())
'''