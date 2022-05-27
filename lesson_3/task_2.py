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
    'девять':'десять'
}
def num_translate(put):
    if put[0].isupper() == True:
        data = dict_number.get ( f'{put.lower()}' )
        print(data.capitalize())
    if put[0].isupper() == False:
        print(dict_number.get(f'{put}',None))

num_translate(input("Введите число по Английски: "))
