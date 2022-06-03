# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном
# списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result  = [number for number in src if src.count(number) == 1]


r = []
for number in src:
    print (f'Количество числа {number} в списке {src.count ( number )} шт' )
    if src.count ( number ) == 1:
        r.append(number)
print(result )
print(r)