result_lst = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in result_lst:
    element_one_lst = list(i.split(' '))
    print("Привет,"+element_one_lst[-1].capitalize()+"!")

