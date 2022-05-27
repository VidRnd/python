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
    print(dict_number.get(f'{put}',None))

num_translate(input("Введите число по Английски: "))
