# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 09:50:23 2021

@author: Ксения Камнева
"""

while True:
    proceeds = input('Введите значение выручки: ')
    costs = input('Введите значение издержек: ')
    try:
        proceeds = float(proceeds)
        costs = float(costs)
        break
    except ValueError:
        print('Неверный формат данных!')

fin_result = proceeds - costs    
if fin_result < 0:
    print(f'\nКомпания работает в убыток. Финансовый результат равен {fin_result:.3f}')
elif fin_result == 0:
    print('\nКомпания работает в нуль.')
else:
    profit = fin_result / proceeds * 100
    print(f'\nУ компании есть прибыль. Финансовый результат равен {fin_result:.3f}\nРентабельность составляет {profit:.3f}%')
    while True:
        strength = input('Введите численность сотрудников фирмы ')
        try:
            strength = int(strength)
        except ValueError:
            print('Неверный формат данных!')
            continue
        if strength > 0:
            break
        print('Введено неверное число')
    num_proceeds = fin_result / strength
    print(f'Прибыль компании в расчете на одного сотрудника составляет {num_proceeds:.3f}')
