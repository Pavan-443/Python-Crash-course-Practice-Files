favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

names = ['Pavan', 'Jen', 'sarah', 'mahesh', 'edward', 'phil', 'jayakar']

for name in names:
    if name not in favorite_languages:
        print(f'\n{name.title()} please take the poll...')
    if name in favorite_languages:
        print(f'\n{name.title()} Thank you for taking the poll...')