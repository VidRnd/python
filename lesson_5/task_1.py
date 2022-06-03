def odd_nums(max_num):
    for num in range ( 1 , max_num ):
        if num % 2 != 0:
            yield num

odd_to_15 = odd_nums(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))









