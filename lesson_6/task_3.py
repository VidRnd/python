from json import dump

with open("users.csv","r",encoding = "utf-8") as user:
    rez_user_lst = []
    for i in user:
        rez_user_lst.append(i.replace(","," ").replace ( "\n" , " " ))
    with open("hobby.csv","r",encoding = "utf-8") as hobby:
        rez_hobby_lst = []
        for i in hobby :
            rez_hobby_lst.append(i.replace(",", " ").replace("\n", " ").split() )

if len(rez_hobby_lst) >= len(rez_hobby_lst):
    n = 0
    rez = {}
    for i in rez_user_lst:
        try:
            rez[i] = rez_hobby_lst[n]
            n += 1
        except IndexError:
            rez[i] = ["None"]
    print(rez)
    with open("rez.json","w",encoding = "utf-8") as rez_json:
        dump(rez,rez_json,ensure_ascii = False, indent=4)
        rez_json.close()
else:
    exit(1)

