import requests
import datetime as dt

def currency_rates(money):
    """Запрашиваем на сайте курс валют
       Принимаем валюту в формате RUB,EUR """
    URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get ( URL )
    answer_json=response.json()
    date_time_str = answer_json['Date']
    date_time_obj = dt.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S%z')
    answer = f"Время: {date_time_obj.strftime('%Y-%m-%d %H:%M:%S')}\nВалюта: {(answer_json['Valute'][f'{money}']['Name'] )}\n" \
             f"Стоимость: {answer_json['Valute'][f'{money}']['Value']} руб"
    return answer

print(currency_rates("ZAR"))

