import cv2
import numpy as np
from sklearn.cluster import KMeans
from tqdm import tqdm
import os
import matplotlib.pyplot as plt
from collections import Counter
from jinja2 import Template

def most_common_colors(color_list, res):
    color_counts = Counter(color_list)
    most_common = color_counts.most_common(res)
    return most_common

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pixels = image.reshape((-1, 3))
    return pixels

def proccess_pixels(hex_colors, res):
    rgb_colors = []
    for hex_color in hex_colors:
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        rgb_colors.append(rgb)
    colors = extract_colors(rgb_colors, res)
    return colors

def extract_colors(pixels, num_colors=5):
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_.astype(int)
    return colors

def plot_colors(color_tuples, save_path=None):
    colors, counts = zip(*color_tuples)
    plt.figure(figsize=(8, 6))
    plt.bar(colors, counts, color=colors)
    plt.xlabel('Colors')
    plt.ylabel('Counts')
    plt.title('Most Common Colors')
    plt.xticks(rotation=45)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

def apply_effect(colors, effect):
    if effect == 'vivid':
        return None
    elif effect == 'pastels':
        return None
    else:
        return colors

def initial_cluster(image_path, effect='standard', suffix=None, name='default', res=5, multiplier=1):
    pixels = preprocess_image(image_path)
    colors = extract_colors(pixels, res*multiplier)
    colors = apply_effect(colors, effect)
    if suffix is not None:
        save_path = f'./data/img/stage1/{name}_{effect}_{suffix}.png'
    else:
        save_path = None
    return colors

def secondary_cluster(hex, effect='standard', suffix=None, name='default', res=5):
    colors = proccess_pixels(hex, res)
    if suffix is not None:
        save_path = f'./data/img/stage2/{name}_{effect}_{suffix}.png'
    else:
        save_path = None
    return colors

def cache(path, package):
    path = './cache/' + path
    package = str(package)
    with open(path, 'w') as file:
        file.write(package)

def rgb_to_hex(rgb):
    r, g, b = rgb
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def proccessImage(image_path, name, resolution=5, cycles=10, depth=100, multiplier=1):
    os.makedirs(f'./cache/{name}/initial_cluster/', exist_ok=True)
    with tqdm(total=depth+1, desc=f'Initial Cluster {name}') as pbar:
        all_color_lists = []
        for i in range(depth+1):
            effect_name = 'standard'
            colors = initial_cluster(image_path, effect_name, i, name, resolution, multiplier)
            for color in colors:
                color = rgb_to_hex(color)
                all_color_lists.append(color)
                cache(f'{name}/initial_cluster/colorlist.txt', all_color_lists)
            pbar.update(1)
    cylce_len = depth*cycles+1
    with tqdm(total=cylce_len, desc=f'Secondary Cluster {name}') as pbar:
        isolated_color_lists = []
        for i in range(cycles):
            for j in range(depth):
                effect_name = 'standard'
                colors = secondary_cluster(all_color_lists, effect_name, f'{i}/{j}', name, resolution)
                for color in colors:
                    color = rgb_to_hex(color)
                    isolated_color_lists.append(color)
                    os.makedirs(f'./cache/{name}/secondary_cluster/', exist_ok=True)
                    cache(f'{name}/secondary_cluster/colorlist.txt', isolated_color_lists)
                pbar.update(1)
    final = most_common_colors(isolated_color_lists, resolution)
    plot_colors(final,f'./data/img/{name}/r{resolution}_c{cycles}_d{depth}_m{multiplier}.jpg')
