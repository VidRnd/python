import requests
import pprint
import  json
import datetime as dt


def currency_rates(money):
    URL = 'https://www.cbr-xml-daily.ru/daily_json.js'

    response = requests.get ( URL )
    h=response.json()
    date_time_str = h['Date']
    date_time_obj = dt.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S%z')
    answer = f"Время: {date_time_obj.strftime('%Y-%m-%d %H:%M:%S')}\nВалюта: {(h['Valute'][f'{money}']['Name'] )}\n" \
             f"Стоимость: {h['Valute'][f'{money}']['Value']} руб"
    return answer

print(currency_rates("ZAR"))

