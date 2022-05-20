duration = int(input())

if int(duration) <= 60 :
    print(str(duration) + " сек")
    if duration == 60:
        print("Или\n1 мин")
elif int(duration) > 60 and int(duration) <= 3600:
    minutes = duration//60
    seconds = duration - minutes*60
    print(str(minutes) + " мин " +str(seconds)+ " сек")
    if duration == 3600:
        print("Или\n1 час")
elif int(duration) > 3600 and int(duration) <= 86400:
    minutes_received = duration // 60
    if minutes_received >= 60 :
        seconds = duration - minutes_received * 60
        hour = minutes_received // 60
        minutes = minutes_received - hour * 60
        print ( str ( hour ) + " час " + str ( minutes ) + " мин " + str ( seconds ) + " сек" )
    if duration == 86400 :
        print ( "Или\n1 день" )
else:
    minutes_received = duration//60
    if minutes_received >= 60:
        hour_received = minutes_received//60
        minutes = minutes_received - hour_received*60
        if hour_received >= 24:
            seconds = duration - minutes_received * 60
            day = hour_received//24
            hour = hour_received - day*24
            print(str(day) +" дн "+str(hour)+" час "+str(minutes) + " мин " +str(seconds)+ " сек")
    if duration == 86400:
        print("Или\n1 день")
