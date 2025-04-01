import asyncio
from PIL import Image, ImageFilter
import os
import time
import matplotlib.pyplot as plt

async def process_image(image_path, output_dir, semaphore):
    async with semaphore:
        img = Image.open(image_path)
        img = img.filter(ImageFilter.BLUR)
        img.save(os.path.join(output_dir, os.path.basename(image_path)))

async def calcular_tempo(threads):
    inicio = time.time()
    input_dir = "input_images"
    output_dir = "output_images"
    os.makedirs(output_dir, exist_ok=True)
    images = [os.path.join(input_dir, img) for img in os.listdir(input_dir) if img.endswith(".jpg")]
    sem = asyncio.Semaphore(threads)
    await asyncio.gather(*(process_image(img, output_dir, sem) for img in images))
    fim = time.time()
    return fim - inicio

async def main():
    tempos = [0]*5
    for _ in range(10):
        for i in range(0, 5):
            tempo = await calcular_tempo(2 ** i)
            tempos[i] += tempo
    for i in range(5):
        tempos[i] = tempos[i]/10
    for i in range(5):
        print(f"{2 ** i} threads: {(tempos[i]/10):.6f} segundos")

    plt.figure(figsize=(8, 6))
    plt.plot(tempos, [(2 ** i) for i in range(0, 5)], marker='o')
    plt.title('Número de Threads x Tempo de Execução')
    plt.xlabel('Segundos')
    plt.ylabel('Número de Threads')
    plt.grid(True)
    plt.savefig("tp2_ex13.png")

if __name__ == "__main__":
    asyncio.run(main())