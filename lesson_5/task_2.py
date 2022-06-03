def odd_nums(max_num):
    """Генерируем нечетные числа от 0 до n, с помощью генератора"""
    rez = (num for num in range(max_num+1) if num % 2 != 0)
    return  rez
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