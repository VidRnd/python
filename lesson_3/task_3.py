def thesaurus(*args):
    rez_key = {}
    for i in args:
        lst = [ ]
        for g in args:
            if i[0] == g[0]:
                lst.append(g)
        if rez_key.get ( f'{i[ 0 ]}' , None ) == None :
            rez_key.update( {i[0]:lst})
    return  rez_key
result = thesaurus ( "Иван" , "Мария" , "Петр" , "Илья" )
print(result)
