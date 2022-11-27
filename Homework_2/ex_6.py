# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 02:31:38 2021

@author: Ксения
"""
from pprint import pprint

name = 'название'
price = 'цена'
quantity = 'количество'
unit = 'единица измерения'
products = []
characteristics = []
product_number = 1

while True:
    product_name = input('Введите название: ')

    try:
        product_price = abs(float(input('Введите цену: ')))
        product_quantity = abs(float(input('Введите количество: ')))
    except ValueError:
        print('Неверный формат данных!')
        continue

    product_unit = input('Введите единицу измерения: ')
    product_data = {
        name: product_name,
        price: product_price,
        quantity: product_quantity,
        unit: product_unit,
    }
    products.append((product_number, product_data))
    characteristics.append(product_data.values())
    product_number += 1
    confirmation = input('Добавить ещё один товар? (да/[нет]) ').lower()
    if confirmation != 'да':
        break

analytics = list(zip(*characteristics))
result = {
    name: list(set(analytics[0])),
    price: list(set(analytics[1])),
    quantity: list(set(analytics[2])),
    unit: list(set(analytics[3])),
}
pprint(result)
    