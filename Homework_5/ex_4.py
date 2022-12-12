"""
Created on Mon May 23 02:12:34 2022

@author: Ксения Камнева
"""
rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open('4n.txt', 'w', encoding='utf-8') as nf:
    with open('4.txt', 'r', encoding='utf-8') as f:
        nf.write(str([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in f]))
