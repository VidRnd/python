
text_1 ="процентов"
text_2 ="процент"
text_3 ="процента"

for percent in range(1,101):

    if percent>=0:
        if percent==0:
            print(str(percent)+" " + text_1)
        elif percent%100>=10 and percent%100<=20:
            print(str(percent)+" " + text_1)
        elif percent%10==1:
            print(str(percent)+" " + text_2)
        elif percent%10>=2 and percent%10<=4:
            print(str(percent)+" " + text_3)
        else:
            print(str(percent)+" " + text_1)
