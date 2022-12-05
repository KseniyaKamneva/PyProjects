# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 00:00:20 2021

@author: Ксения Камнева
"""

def account_info(
    first_name=None,
    last_name=None,
    year=None,
    city=None,
    email=None,
    phone=None,
):
    return(f'{first_name} {last_name}, {year}, {city}, {email}, {phone}.')

first_name = input('Введите имя: ')
last_name = input('Введите фамилию: ')
year = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите email: ')
phone = input('Введите номер телефона: ')
print(account_info(first_name, last_name, year, city, email, phone))
