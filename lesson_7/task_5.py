import os
directory = 'C:\телефон лена 04.09.2021'

rez =  {
      '100':  ("0",[]),
      '1000':  ("0",[]),
      '10000':  ("0",[]),
      '100000': ("0",[])
    }
format_100 = set ( )
format_1000 = set ( )
format_10000 = set ( )
format_100000 = set ( )

for dirpath, dirnames, filenames in os.walk(directory,"."):
    count_all = 0
    for filename in filenames:
        d = os.path.getsize ( os.path.join ( dirpath , filename ) )
        g = os.path.join(dirpath, filename)
        format_files = str(g).split("." )[-1]
        if d < 100 :
            count = rez.get('100')
            count_all += int ( count[ 0 ] ) + 1
            format_100.add ( format_files )
            count_t = (f'{count_all},{list ( format_100 )}')
            rez[ '100' ] = count_t
        elif d < 1000 :
            count = rez.get('1000')
            count_all += int(count[0]) + 1
            format_1000.add(format_files)
            count_t = (f'{count_all},{list ( format_1000 )}')
            rez[ '1000' ] = count_t
        elif d < 10000 :
            count = rez.get('10000')
            count_all += int(count[0]) + 1
            format_10000.add(format_files)
            count_t = (f'{count_all},{list(format_10000)}')
            rez['10000'] = count_t
        elif d < 100000 :
            count = rez.get('100000')
            count_all += int(count[0]) + 1
            format_100000.add(format_files)
            count_t = (f'{count_all},{list(format_100000)}')
            rez['100000'] = count_t

print ( rez )
