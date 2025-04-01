import time
import matplotlib.pyplot as plt
import asyncio
import aiohttp

async def ex1():
    urls = ["https://darksouls2.wiki.fextralife.com/Lore",
            "https://www.reddit.com/r/DarkSouls2/comments/6ng896/summary_of_dark_souls_2_lore",
            "https://www.quora.com/Could-you-explain-the-lore-of-Dark-Souls-2",
            "https://en.wikipedia.org/wiki/Dark_Souls_II",
            "https://steamcommunity.com/sharedfiles/filedetails/?id=1436671498",
            "https://fextralife.com/dark-souls-2-total-lore-and-location-breakdown/",
            "http://soulslore.wikidot.com/dark-souls2",
            "https://www.reddit.com/r/DarkSouls2/comments/ld257b/dark_soul_2s_lore_is_integral_to_the_series_why",
            "https://darksouls2.wiki.fextralife.com/About+Dark+Souls+2",
            "https://darksouls2.wiki.fextralife.com/Bosses", "https://darksouls2.wiki.fextralife.com/Merchants",
            "https://darksouls2.wiki.fextralife.com/Equipment+&+Magic", "https://darksouls2.wiki.fextralife.com/Magic",
            "https://darksouls2.wiki.fextralife.com/Armor",
            "https://darksouls2.wiki.fextralife.com/Weapons", "https://darksouls2.wiki.fextralife.com/Shields"]

    tempos = []

    async def download_url(session, url, sem):
        async with sem:
            async with session.get(url) as response:
                content = await response.text()
                print(f"Downloaded {url}: {len(content)} bytes")

    async def calcular_tempo(threads):
        inicio = time.time()
        sem = asyncio.Semaphore(threads)
        async with aiohttp.ClientSession() as session:
            await asyncio.gather(*(download_url(session, url, sem) for url in urls))
        fim = time.time()
        return fim - inicio

    print(f"Número de URLs: {len(urls)}")
    for i in range(0, 5):
        tempo = await calcular_tempo(2 ** i)
        tempos.append(tempo)
        print(f"{2 ** i} threads: {tempo:.4f} segundos")

    plt.figure(figsize=(8, 6))
    plt.plot(tempos, [(2 ** i) for i in range(0, 5)], marker='o')
    plt.title('Número de Threads x Tempo de Execução')
    plt.xlabel('Segundos')
    plt.ylabel('Número de Threads')
    plt.grid(True)
    plt.savefig("tp2_ex11.png")


if __name__ == "__main__":
    asyncio.run(ex1())