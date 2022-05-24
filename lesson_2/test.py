duration = int(input('Enter the number '))
seconds = duration % 60
minutes = duration // 60
hours = duration // 3600
days = duration // 86400

if duration < 60:
    print('Time', ':', seconds, 'sec')
elif duration <= 3600:
    print('Time', ':', hours, 'h', minutes, 'min', seconds, 'sec')
else:
    print('Time', ':', days, 'd', hours, 'h', minutes, 'min', seconds, 'sec')