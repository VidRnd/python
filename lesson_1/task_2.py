sum_all = 0
sum_plus = 0
num_list = []
for i in range(1,1001):
    num = i**3
    if num % 2 > 0 :
        num_list.append(num)
for num in num_list:
    num_for_sum = (num)
    suma_num = 0
    while num > 0:
        digit = num % 10
        suma_num = suma_num + digit
        num = num // 10
    if suma_num%7 == 0:
        print(suma_num)
        sum_all = sum_all + num_for_sum
    num_plus = int(str(num_for_sum)+"17")
    print(num_plus)
    suma_num = 0
    while num > 0 :
        digit = num % 10
        suma_num = suma_num + digit
        num = num // 10
    if suma_num%7 == 0 :
        sum_plus = sum_plus + num_plus
print("Сумма -", sum_all)
print("Сумма добавляем '17' к каждому числу -", sum_plus)
# print(num_list)





