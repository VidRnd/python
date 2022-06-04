src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
rezult = [number_right for number, number_right in zip(src, src[1:]) if number_right > number]
print(rezult )














