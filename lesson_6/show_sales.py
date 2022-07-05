from sys import argv
with open("all.txt",'r',encoding = "utf-8") as all:
    if len(argv) == 1:
            print(all.read())

    if len(argv) == 2:
        for pos , l_num in enumerate ( all) :
            if pos >= (int(argv[1])-1) :
                print ( str(l_num).replace('\n','') )

    if len(argv) == 3:
        for pos , l_num in enumerate ( all) :
            if (int(argv[2])) > pos >= (int(argv[1])-1) :
                print ( str(l_num).replace('\n','') )