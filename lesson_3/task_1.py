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
    """Переводит слова с Английского на русский от 1 до 10"""
    print(dict_number.get(f'{put}',None))

num_translate(input("Напишите чило по  Английски от 1 до 10: "))
