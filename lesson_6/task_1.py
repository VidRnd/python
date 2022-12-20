lst = []
with open ( "nginx_logs.txt" , "r" , encoding = "utf-8" ) as rez:
    for line in rez:
        content = (line.split()[0], line.split()[5], line.split()[6])
        lst.append(content)
print(lst)

