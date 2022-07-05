dict_number = {
    'one':'один',
    'two': 'два',
    'three':'три',
    'four':'четыре',
    'five':'пять',
    'six':'шесть',
    'seven':'семь',
    'eight':'восемь',
    'nine':'девять',
    'ten':'десять'
}
def num_translate(put):
    """Переводит слова с Английского на русский от 1 до 10, ответ отправляет в регистре первой буквы в запросе"""
    if put[0].isupper() == True:
        data = dict_number.get ( f'{put.lower()}' )
        print(data.capitalize())
    if put[0].isupper() == False:
        print(dict_number.get(f'{put}',None))

num_translate(input("Введите число по Английски: "))
