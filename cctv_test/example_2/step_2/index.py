# import asyncio
# import random

# async def simulate_movement(seconds, frame_rate):
#     total_frames = frame_rate * seconds
#     positions = []

#     for _ in range(total_frames):
#         x = random.uniform(-100, 100)
#         y = random.uniform(-100, 100)
#         positions.append((x, y))
#         await asyncio.sleep(1 / frame_rate)  # Simulira čekanje na izvršavanje jednog frame-a

#     return positions

# async def main():
#     frame_rate = 30
#     seconds = 5
#     positions = await simulate_movement(seconds, frame_rate)
#     print(positions)

# if __name__ == '__main__':
#     asyncio.run(main())

import asyncio
import random

async def simulate_movement(seconds, frame_rate):
    total_frames = frame_rate * seconds
    positions = []

    for _ in range(total_frames):
        x = random.uniform(-100, 100)
        y = random.uniform(-100, 100)
        positions.append((x, y))
        await asyncio.sleep(1 / frame_rate)  # Simulira čekanje na izvršavanje jednog frame-a

    return positions

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

    # Pohranjivanje rezultata u varijablu positions
    positions = results

    # Ispisivanje ukupanog broja pozicija generiranih
    total_positions = sum(len(pos_list) for pos_list in positions)
    print(f"Ukupan broj pozicija koje su generirane: {total_positions}")

if __name__ == '__main__':
    asyncio.run(main())
