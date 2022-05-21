sum_all = 0
sum_plus = 0
for i in range(1,1001):
    num = (i**3)
    suma_num = 0
    while num > 0:
        digit = num % 10
        suma_num = suma_num + digit
        num = num // 10
    if suma_num%7 == 0 :
        sum_all = sum_all + i
    num = int(str(i**3)+"17")
    suma_num = 0
    while num > 0 :
        digit = num % 10
        suma_num = suma_num + digit
        num = num // 10
    if suma_num%7 == 0 :
        sum_plus = sum_plus + i
print("Сумма ", sum_all)
print("Сумма добавляем '17' к каждому числу) -", sum_plus)





