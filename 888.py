from utitless import *
from untitlesss import *

print('Привет, выбери приветствие или шутку, факт')

while True:
    уу = input("Введи слово(приветствие, шутка, факт)")
    if yy != 'стоп':
        if yy == 'приветствие':
            print(generate_greeting)
        elif yy == 'шутка':
            print(get_random_joke)
        elif yy == 'факт':
            print(get_random_joke1)
    else:
        break