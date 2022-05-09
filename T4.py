# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 1 до 100, можно создать свой генератор случайных чисел или
# использовать готовый) многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# k=2 => 2*x² + 4*x + 5 = 0
# 3*х^2 + 2*x + 5

# импорт библиотеки для генерации случайных чисел
from random import randint

# путь к файлу
path = 'file.txt'

# открытие файла для записи
data = open(path, 'a')

# запрашиваем у пользователя натуральную степень k 
k = int(input('Input k: '))

for i in range(0, k):
    if(i < (k - 1)):
        data.write(f'{randint(1, 100)}*x^{k-i} + ')
    if(i == (k - 1)):
        data.write(f'{randint(1, 100)}*x + {randint(1, 100)} = 0\n')
data.close()
