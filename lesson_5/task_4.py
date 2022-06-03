# ### 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# -----------------Способ 1
m = [number_right for number, number_right in zip(src, src[1:]) if number_right > number]
print("Результат через генератор",m)
# -----------------Способ 2
g = []
for number,number_right in zip(src, src[1:]):
    print("Список минус предыдущий элемент",src[ 1 : ])
    print(number)
    print ( number_right )
    if number_right > number:
        g.append(number_right)

print("Результат через цикл",g)














# -----------------Способ 3
d =[]
def rezult_number(src):

    for number , number_right in zip ( src , src[ 1 : ] ) :

        if number_right > number :
            d.append(number_right)
            yield number_right
odd_to_15 = rezult_number(src)
print(odd_to_15) #Доказать, что вы создали именно генератор
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(d)
