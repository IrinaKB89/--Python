"""
Для списка реализовать обмен значений соседних элементов.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
При нечётном количестве элементов последний сохранить на своём месте.
Для заполнения списка элементов нужно использовать функцию input()
"""
my_list = input("Введите целые числа через пробел: ").split(' ')
i, j = 0, 1
while len(my_list) > j:
    my_list[i], my_list[j] = my_list[j], my_list[i]
    i += 2
    j += 2
print('Результат:', *my_list)
