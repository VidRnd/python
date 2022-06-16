import requests
import re
import time
URL = "https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
rez = requests.get(URL)
with open("rez.txt", 'w+', encoding = 'utf-8') as file:
    file.write(rez.text)
with open("rez.txt", 'r', encoding = 'utf-8') as file:
#     rez = file.read()
#     print(file)
    for i in file:
        # print(i)
        # print(rez.text)
        # ip = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\ )',rez.text)
        # date = re.findall(r'\d+[/]\w+[/].+\d{4}',rez.text)
        date = re.findall(r'(\d+[/]\w+[/].+\d{4})',i)
        get = re.findall(r'"([A-Z]{3})',i)
        # path = re.findall(r'(/d.+?)\s', i)
        nub = re.findall(r'\s(\d+)\s',i)
        # print(date)
        rez =re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*\[(.+\d{4}).*"([A-Z]{3}).*(/d.+?)\s.*\s(\d+)\s(\d+) ',i)
        # print(rez)
        if not rez:
            rez = re.findall(r'(^\w{4}:.+\:\w{4}).*\[(.+\d{4}).*"([A-Z]{3}).*(/d.+?)\s.*\s(\d+)\s(\d+)',i)
            print("--------",rez)
            # print(i)
            # time.sleep(5)
            if not rez:
                print("-===========", i)
#         print(rez)
#         break
# #
