rivers = {
    'nile': 'egypt',
    'godavari': 'india',
    'indus': 'pakistan'
}

for river in sorted(rivers.keys()):
    print(f'{river.title()} flows through {rivers[river].title()}')

print('\nRivers are:')
for keys in sorted(rivers):
    print(f'{keys.title()}')

print('\ncountries are:')
for values in sorted(rivers.values()):
    print(f'{values.title()}')