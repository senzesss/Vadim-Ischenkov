# Вариант 11.
# В магазинах имеются следующие товары. Магнит – молоко, соль, сахар, печенье, сыр.
# Пятерочка – мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар, печенье. Лента
# – печенье, молоко, сыр.
# Определить:
# 1. в каких магазинах нельзя приобрести соль.
# 2. в каких магазинах можно приобрести одновременно молоко, печенье и сыр.
# 3. в каких магазинах можно приобрести мясо и молоко.



magnet = {'молоко', 'соль', 'сахар', 'печенье', 'сыр'}
pyatero4ka = {'мясо', 'молоко', 'сыр'}
perekrestok = {'молоко', 'творог', 'сыр', 'сахар', 'печенье'}
lenta = {'печенье', 'молоко', 'сыр'}


notsol = set()
mps = set()
myaso = set()
moloko = set()

if 'соль' not in magnet:
    notsol.add('Магнит')
if 'соль' not in pyatero4ka:
    notsol.add('Пятёрочка')
if 'соль' not in perekrestok:
    notsol.add('Перекрёсток')
if 'соль' not in lenta:
    notsol.add('Лента')

if ('молоко' in magnet) and ('печенье' in magnet) and ('сыр' in magnet):
    mps.add('Магнит')
if ('молоко' in pyatero4ka) and ('печенье' in pyatero4ka) and ('сыр' in pyatero4ka):
    mps.add('Пятёрочка')
if ('молоко' in perekrestok) and ('печенье' in perekrestok) and ('сыр' in perekrestok):
    mps.add('Перекрёсток')
if ('молоко' in lenta) and ('печенье' in lenta) and ('сыр' in lenta):
    mps.add('Лента')

if 'мясо' in magnet:
    myaso.add('Магнит')
if 'мясо' in pyatero4ka:
    myaso.add('Пятёрочка')
if 'мясо' in perekrestok:
    myaso.add('Перекрёсток')
if 'мясо' in lenta:
    myaso.add('Лента')

if 'молоко' in magnet:
    moloko.add('Магнит')
if 'молоко' in pyatero4ka:
    moloko.add('Пятёрочка')
if 'молоко' in perekrestok:
    moloko.add('Перекрёсток')
if 'молоко' in lenta:
    moloko.add('Лента')


print(f'Магазины в которых нет соли: {notsol}')
print(f'Магазины в которых можно купить молоко, печенье и сыр сразу: {mps}')
print(f'Магазины в которых можно купить мясо: {myaso}')
print(f'Магазины в которых можно купить молоко: {moloko}')
