print('>>>>>>>>')
# 3557 К.Ю.Поляков
'''
Решите уравнение 103x + 11 = 103x+1. Ответ запишите в десятичной системе счисления. P.S. смотрите условие на сайте
'''

for num in range(3, 10):  # почему от 3? потому что есть запись 121, 2 может быть только от троичной сс
    if int('121', num) + 1 == 82:
        print(num)
# print(int('121', 8))

for num_2 in range(3, 10):
    if (1 * num_2 ** 0) + (2 * num_2 ** 1) + (1 * num_2 ** 2) + 1 == (1 * 9 ** 0) + (0 * 9 ** 1) + (1 * 9 ** 2):
        # num_2 ** 0 == 1, num_2**1 == num_2,                       1 + 0 + 82
        if 1 + (2 * num_2) + num_2 ** 2 + 1 == 82:
            print(num_2)
