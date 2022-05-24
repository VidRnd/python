rezult_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
answer_one = ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
answer_two = 'в "05" часов "17" минут температура воздуха была "+05" градусов'
for i in rezult_list[:]:
    index_rez_lst = rezult_list.index ( f"{i}" )
    if i[0] == '+':
        i_plus = i.replace('+', '', 1)
        rezult_list[ index_rez_lst ] = "+0" + str ( i_plus )
        rezult_list.insert ( index_rez_lst , '"' )
        rezult_list.insert ( index_rez_lst + 2 , '"' )

    elif i.isdigit() == True:

        if len(i) == 1:
            rezult_list[ index_rez_lst ] = "0" + str ( i )
            rezult_list.insert( index_rez_lst, '"')
            rezult_list.insert ( index_rez_lst + 2 , '"' )

        else:
            print(index_rez_lst,i)
            rezult_list.insert ( index_rez_lst , '"' )
            rezult_list.insert ( index_rez_lst + 2 , '"' )

print("Должно получится\n",answer_one)
print(rezult_list)
print("Должно получится\n",answer_two)
print(" ".join(rezult_list))
