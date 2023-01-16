biogsuku = str(input('Mikä on biologinen sukupuolesi: '))
hemoglob = float(input('Mikä on hemoglobiiniarvosi(g/l): '))

if biogsuku == 'Nainen':
    if hemoglob<117:
        print('Hemoglobiiniarvosi on alhainen.')
    elif hemoglob>175:
        print('Hemoglobiiniarvosi on korkea.')
    else:
        print('Hemoglobiiniarvosi on normaali.')

if biogsuku == 'Mies':
    if hemoglob<134:
        print('Hemoglobiiniarvosi on alhainen.')
    elif hemoglob>195:
        print('Hemoglobiiniarvosi on korkea.')
    else:
        print('Hemoglobiiniarvosi on normaali.')