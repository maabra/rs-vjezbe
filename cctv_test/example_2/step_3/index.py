import aiohttp
import asyncio
import random
from cctv import CCTV_frame

async def simulate_movement(seconds, frame_rate):
    total_frames = frame_rate * seconds
    positions = []

    for _ in range(total_frames):
        x = random.uniform(-100, 100)
        y = random.uniform(-100, 100)
        positions.append((x, y))
        await asyncio.sleep(1 / frame_rate)  # Simulira čekanje na izvršavanje jednog frame-a

    return positions

async def update_camera_location(instance, x, y):
    instance.update_location(x, y)
    print(instance.info())

async def main():
    frame_rate = 30

    # Testiranje korutine simulate_movement za 5 sekundi
    print("Testing simulate_movement for 5 seconds:")
    positions = await simulate_movement(5, frame_rate)
    print(positions)

    # Konkurentno pozivanje korutine 5 puta za 1, 2, 3, 4, 5 sekundi simuliranja
    durations = [1, 2, 3, 4, 5]
    tasks = [simulate_movement(seconds, frame_rate) for seconds in durations]
    results = await asyncio.gather(*tasks)

    # Normalizacija liste positions
    positions = [pos for sublist in results for pos in sublist]

    # Uzimanje prvih 50 pozicija
    first_50_positions = positions[:50]

    # Kreiranje instance CCTV_frame
    cctv_frame = CCTV_frame(
        frame_id=1,
        location_x=0,
        location_y=0,
        frame_rate=30,
        camera_status="Active",
        zoom_level=1,
        ip_address="192.168.1.1"
    )

    # Pozivanje korutine update_camera_location za svaku poziciju iz liste first_50_positions
    update_tasks = [update_camera_location(cctv_frame, x, y) for x, y in first_50_positions]
    await asyncio.gather(*update_tasks)

    # Ispisivanje ukupnog broja pozicija generiranih
    total_positions = len(positions)
    print(f"Ukupan broj pozicija koje su generirane: {total_positions}")

    # Klijentska sesija i slanje 50 konkurentnih zahtjeva prema endpointu /cctv
    async with aiohttp.ClientSession() as session:
        cctv_tasks = [
            session.post('http://localhost:8090/cctv', json={
                "location_x": x,
                "location_y": y,
                "frame_rate": 30,
                "camera_status": "Active",
                "zoom_level": 1,
                "ip_address": "192.168.1.1"
            }) for x, y in first_50_positions
        ]
        responses = await asyncio.gather(*cctv_tasks)
        for response in responses:
            print(await response.json())

if __name__ == '__main__':
    asyncio.run(main())

