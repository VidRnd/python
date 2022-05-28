def thesaurus_adv(*args):
    """ Принимаем кортеж Имя Фамилия. Возвращает сортировку по первой букве фамилии и по первой букве имени"""
    rez_sorting = {}
    user_lst = []
    for i in args:
        user_lst.append( i.split(' '))
    for surname in user_lst :
        key = surname[1][0]
        if key not in rez_sorting :
            rez_sorting[ key ] = [ ]
        rez_sorting[ key ].append ( surname )
    for i in rez_sorting.keys():
        res1 = {}
        for g in rez_sorting[i]:
            key1 = g[ 0 ][ 0 ]
            if key1 not in res1 :
                res1[ key1 ] = [ ]
            connect_text= g[0]+", "+g[1]
            res1[key1].append (connect_text )
        rez_sorting[i]=(res1)
    return rez_sorting

result = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

print(result)

