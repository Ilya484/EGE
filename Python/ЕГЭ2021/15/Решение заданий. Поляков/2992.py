print('>>>>>>>')
#2992 К.Ю.Поляков
'''
Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m». 
Для какого наименьшего натурального числа A формула
((ДЕЛ(x, A) ∧ ДЕЛ(x, 36)) → ДЕЛ(x, 324)) ∧ (A > 100)
тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)? 
'''
for a in range(1, 7290+1): # 45 * 162 = 7290
    good = True
    for x in range(1, 7290*100+1):  # P.S. делайте большой диапозон, иначе будете сидеть весь день как я
        if (  (( (x % a == 0) and (x % 45 == 0) ) <= (x % 162 == 0) ) and (a > 200)  ) == 0:
            good = False
            break
    if good:
        print(a)
        break
