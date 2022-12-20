def thesaurus_adv(*args):
    """ Принимаем кортеж Имя Фамилия. Возвращает сортировку по первой букве фамилии и по первой букве имени"""
    rez_sorting = {}
    user_lst = []
    for i in args:
        user_lst.append( i.split(' '))
    for surname in user_lst :
        key_surname = surname[1][0]
        if key_surname not in rez_sorting :
            rez_sorting[key_surname] = []
        rez_sorting[key_surname].append(surname)
    for i in rez_sorting.keys():
        res_sort_name = {}
        for g in rez_sorting[i]:
            sort_name = g[ 0 ][ 0 ]
            if sort_name not in res_sort_name :
                res_sort_name[ sort_name ] = []
            connect_text= g[0]+", "+g[1]
            res_sort_name[sort_name].append (connect_text )
        rez_sorting[i]=(res_sort_name)
    return rez_sorting

result = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

print(result)

