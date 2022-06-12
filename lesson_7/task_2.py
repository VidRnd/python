import os
import re
import os

global FIRST_LVL_THREE
global TWO_LVL_THREE
global THREE_LVL_THREE
global FOUR_LVL_THREE

h=open('config.yaml','r',encoding = 'utf-8')

def func ():
    """Читаем построчно файил, определяем лес папок максимум 3 сложения в папки"""
    line = h.readline()
    if line[0:3] == '|--':
        rez = [f"{line.replace('|--','')}","1"]
        return rez
    elif line[0:6] == '   |--' :
        rez = [ f"{line.replace('   |--','')}" , "2" ]
        return rez
    elif line[0:9] == '   |  |--':
        rez = [ f"{line.replace('   |  |--','')}" , "3" ]
        return rez
    elif line[0:12] == '   |     |--':
        rez = [ f"{line.replace ( '   |     |--' , '' )}" , "4" ]
        return rez
    elif line[0:15] == '   |        |--':
        rez = [ f"{line.replace ( '   |        |--' , '' )}" , "5" ]
        return rez
    else:
        if not line:
            return
        else:
            rez = [ f"{line}" , "10" ]
            return rez
def creating_folders(path):
    """Создаем папку"""
    os.makedirs ( path , exist_ok = True )
def creating_file(path):
    """Создаем файл"""
    with open(path,'w') as new_file:
        new_file.close()

while True:
    request=func()
    if not request:
        print("--------------------------------КОНЕЦ--------------------------------")
        break
    if int(request[1]) == 1:
        FIRST_LVL_THREE = (request[0]).replace('\n','')
        creating_folders (FIRST_LVL_THREE)

    elif int(request[1]) == 2:
        folder = str(request[0]).replace("\n","")
        path = f'{FIRST_LVL_THREE}/{folder}'
        if re.search(r'[.]', folder):
            creating_file(path)
        else:
            TWO_LVL_THREE = folder
            creating_folders(path)
        print(path)

    elif int(request[1]) == 3:
        folder = str (request[0]).replace ("\n","")
        path = f'{FIRST_LVL_THREE}/{TWO_LVL_THREE}/{folder}'
        if re.search(r'[.]',folder):
            creating_file(path)
        else:
            THREE_LVL_THREE = folder
            creating_folders(path)
        print (path)
    elif int(request[1]) == 4 :
        folder = str ( request[ 0 ] ).replace ( "\n" , "" )
        path = f'{FIRST_LVL_THREE}/{TWO_LVL_THREE}/{THREE_LVL_THREE}/{folder}'
        if re.search(r'[.]', folder):
            creating_file ( path )
        else:
            FOUR_LVL_THREE = folder
            creating_folders(path)
        print(path)
    elif int(request[1]) == 5 :
        folder = str ( request[ 0 ] ).replace ( "\n" , "" )
        path = f'{FIRST_LVL_THREE}/{TWO_LVL_THREE}/{THREE_LVL_THREE}/{FOUR_LVL_THREE}/{folder}'

        if re.search(r'[.]', folder):
            creating_file(path)
        else:
            THREE_LVL_THREE = folder
            creating_folders(path)
        print(path)
    else:
        print("Вложенность больше чем может обработать программа", request)
        break