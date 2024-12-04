import asyncio
import aiohttp
# import microservice_1
# import microservice_2
async def fetch_service1():
  async with aiohttp.ClientSession() as session:
    response = await session.get('http://localhost:8081/')
    return await response.json()

async def fetch_service2():
  async with aiohttp.ClientSession() as session:
    response = await session.get('http://localhost:8082/')
    return await response.json()
  
async def main():
    print("Pokrećem main korutinu")
    responses = await asyncio.gather(fetch_service1(), fetch_service2())
#   service1_response = await fetch_service1()
#   print(f"Odgovor mikroservisa 1: {service1_response}")

#   service2_response = await fetch_service2()
#   print(f"Odgovor mikroservisa 2: {service2_response}")
    print(responses)


asyncio.run(main())
