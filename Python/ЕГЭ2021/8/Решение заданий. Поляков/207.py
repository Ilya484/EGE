from itertools import *
print('>>>>>>')
# 207 К.Ю.Поляков
'''
Вася составляет 5-буквенные слова, в которых есть только буквы С, Л, О, Н, 
причём буква С используется в каждом слове ровно 1 раз. 
Каждая из других допустимых букв может встречаться в слове любое количество раз или не встречаться совсем. 
Словом считается любая допустимая последовательность букв, не обязательно осмысленная. 
Сколько существует таких слов, которые может написать Вася? 
'''

def ok(x): #реализация через функция, удобно, используйте
    if x.count('С') == 1:
        return True
    else:
        return False
s_waw = 'СЛОН'
m = {x for x in product(s_waw, repeat=5) if ok(x)} #генератор
print(len(m))
