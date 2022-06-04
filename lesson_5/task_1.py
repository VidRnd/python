def odd_nums(max_num):
    """Генерируем нечетные числа от 0 до n, с помощью генератора"""
    for num in range ( 0 , max_num+1 ):
        try:
            if num % 2 != 0:
                yield num
        except StopIteration:
            print("dddddd")
            return

odd_to_15 = odd_nums(15)
print(odd_to_15)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))









