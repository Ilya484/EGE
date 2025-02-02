from functools import lru_cache #импорт встроенной библиотеки



print('>>>>>>>>>> Прога для 19ых. Измените условие для 20-21 и возьмите пирожок \n >>>>>>')
#К.Ю.Поляков 4207
'''
Условие: https://prnt.sc/1bd5n37 
'''
# 'h' - большая пещера, где хранятся камешки. Там может быть 1 куча, а может и 3)
def move(h): #функция для подсчета всевозможных ходов в кучах
    a, b, c = h # 3 кучи из условия задачи
    return (a+3, b, c), (a, b+3, c), (a, b, c+3), (a+13, b, c), (a, b+13, c), (a, b, c+13), \
           (a+23, b, c), (a, b+23, c), (a, b, c+23) #подсчет


@lru_cache(None) #кэширование. т.е. сохранение промеж. результатов при счете
def f(h): # проверка на победу 
    if sum(h) >= 73:
        return 'WIN'
    elif any( f(m) == 'WIN' for m in move(h)):
        return 'P1'
    elif any( f(m) == 'P1' for m in move(h)):
        return 'B1'
    elif any( f(m) == 'B1' for m in move(h)):
        return 'P2'
    elif all( f(m) == 'P2' or f(m) == 'P1' for m in move(h)):
        return 'V2'
for i in range(1, 23+1): # из условия s - от 1, до 23. помним специфику цикла в питоне
    print(i, f((2, i, i*2))) # (( )) #т.к. на выходе кортежи


'''
19:
elif any( f(m) == 'P1' for m in move(h)):
        return 'B1'
20-21:
elif all( f(m) == 'P1' for m in move(h)):
        return 'B1'
Читайте задание внимательно, иногда немного другие условия
'''