# encoding: utf-8 

from datetime import date

"""
Simple program who ask year of the birthday and return subtract from current year
"""

print('Доброго дня.')
year = input('Введіть рік Вашого народження: ')

today = date.today()

if year.isdigit():
    if int(year) > today.year:
        print('Ви з майбутнього?')
    elif int(year) < today.year - 150:
        print('Статистично дуже малоймовірно, що Вам більше 150-ти років.')
    else:
        print(f'Наразі {today.year} рік: {today.year} - {year} = {today.year - int(year)}')
else:
    print(f'{year} - рік народження може бути лише цілим числом!')

