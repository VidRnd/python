all_ip_lst = []
spam_ip = ["0","0"]
with open('nginx_logs.txt', 'r', encoding = 'utf-8') as rez:
    while True:
        line = rez.readline()
        if not line:
            break
        all_ip_lst.append(line.split()[0])
    for ip in set(all_ip_lst):
        if all_ip_lst.count(ip) > int( spam_ip[1]):
            spam_ip = [f'{ip}',all_ip_lst.count(ip)]
    print(f'Спамер! - IP {spam_ip[0]} количество запросов {spam_ip[1]}')

