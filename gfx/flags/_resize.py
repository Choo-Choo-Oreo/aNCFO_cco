#!/usr/bin/env python

from PIL import Image
import os
from multiprocessing import Pool, cpu_count

def process_image(filename):
    os.makedirs('medium', exist_ok=True)
    os.makedirs('small', exist_ok=True)
    try:
        with Image.open(filename) as img:
            img.resize((41, 26)).save(os.path.join('medium', filename))
            img.resize((10, 7)).save(os.path.join('small', filename))
    except Exception as e:
        print(f"Error processing {filename}: {e}")

if __name__ == '__main__':
    files = [f for f in os.listdir('.') if f.lower().endswith('.tga')]
    with Pool(cpu_count()) as p:
        p.map(process_image, files)
