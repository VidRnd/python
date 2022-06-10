from sys import argv

if len ( argv ) == 1 :
    with open ( "all.txt" , "r" , encoding = "utf-8" ) as all1 :
        print ( all1.read ( ) )

if len(argv) > 1:
    with open ( "all.txt" , "a+" , encoding = "utf-8" ) as all :
        rez=argv[1].replace(',','').replace('.','')
        if len( [i for i in rez if i.isdigit() ] ) == len(rez):
            rez = round(float(argv[1].replace(',','.')),1)
            all.write(str(rez).replace('.',',')+'\n')
            print("pddd",rez)
        else:
            print("Введи цену цифрами")
