# encoding: utf-8 

"""
Simple program who ask user years old and return subtract from current year
"""

print('Доброго дня.')
years_old = input('Введіть к-сть Ваших повних років: ')

if years_old.isdigit():
    print(f'Наразі 2021 рік: 2021 - {years_old} = {2021 - int(years_old)}')
else:
    print(f'{years_old} - к-сть повних років може бути лише цілим числом!')

