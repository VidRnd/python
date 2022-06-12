import os
directory = 'some_data'

rez =  {
      '100': 0,
      '1000': 0,
      '10000': 0,
      '100000': 0
    }

for dirpath, dirnames, filenames in os.walk(directory,"."):
    for filename in filenames:
        d = os.path.getsize(os.path.join(dirpath, filename))
        if d < 100 :
            count = rez.get ('100')
            rez['100'] = count + 1
        elif d < 1000:
            count = rez.get('1000')
            rez['1000'] = count + 1
        elif d < 10000 :
            count = rez.get('10000')
            rez['10000'] = count + 1
        elif d < 100000 :
            count = rez.get ( '100000' )
            rez['100000'] = count + 1
    print(rez)

