print('>>>>>>>')
#К.Ю.Поляков 3994
'''
Рассматривается множество целых чисел, принадлежащих числовому отрезку
[4616; 52311],которые удовлетворяют следующим условиям:
а) Сумма цифр равна 10.
б) Произведение цифр равно нулю.
Найдите количество таких чисел и минимальное из них. В ответе запишите
сначала количество, а затем минимальное из них. 
'''

count = 0
mina = float('inf')
for x in range(4616, 52311+1): #+1 ОБЯЗАТЕЛЬНО
    if sum(map(int, str(x))) == 10 and [i for i in list(map(int, str(x))) if i==0]:
        count +=1
        mina = min(x, mina)
print(count, mina)