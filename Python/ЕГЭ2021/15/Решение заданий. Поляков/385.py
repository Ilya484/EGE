print('>>>>>>>')

#К.Ю.Поляков 385 
'''
 Элементами множеств А, P, Q являются натуральные числа, причём P={1,3,7},
 Q={1,2,4,5,6}. Известно, что выражение
((x ∉ A) → (x ∉ P)) ∨ ((x ∉ Q) ∧ (x ∈ P))
истинно (т.е. принимает значение 1 при любом значении переменной х.
Определите наименьшее возможное количество элементов в множестве A. 
'''

p = {1, 3, 7}
q = {1, 2, 4, 5, 6}

def f(x, a):
     return  ((x not in  a) <= (x not in p)) or ((x not in q) and (x in p))

a = set()#если найти наименьшее, то мы ничего не делаем и прибавляем 'x' по необ.
for x in range(1, 1000):
    if not f(x, a):
        a.add(x)
        '''если не выполняется, то добавляем х.
         Если 'x in a' и такого х нету,
                 то мы добавляем его для того чтобы выполнялось.
                 Если 'x not in a', то ничего не делаем, итак выпоняется.'''
        
print(sorted(a))
