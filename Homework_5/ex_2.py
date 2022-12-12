"""
Created on Mon May 23 01:32:04 2022

@author: Ксения Камнева
"""

with open('2.txt', 'r', encoding='utf-8') as f:
    usefulness = [f'{num}. {" ".join(line.split())} - {len(line.split())} слов ' for num, line in enumerate(f, 1)]
    print(*usefulness, f'Всего строк - {len(usefulness)}.', sep='\n')
