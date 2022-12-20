from random import randint

def get_jokes(count):
    """Принимаем число. Возврашаем три случайных значения из всех словарей """
    nouns = [ "автомобиль" , "лес" , "огонь" , "город" , "дом" ]
    adverbs = [ "сегодня" , "вчера" , "завтра" , "позавчера" , "ночью" ]
    adjectives = [ "веселый" , "яркий" , "зеленый" , "утопичный" , "мягкий" ]
    rez = []
    for i in range ( count ) :
        rez_text = (str(nouns[int(randint ( 0 , int(len(nouns)-1) ))]) +" "+
              str(adverbs[int(randint ( 0 , int(len(adverbs)-1) ))])+" "+
              adjectives[int(randint ( 0 , int(len(adjectives)-1) ))])
        rez.append(rez_text)
    return rez

reg = get_jokes(2)
print(reg)
