guests = ['jayakar', 'rudheer', 'varshith', 'vikash']
message = 'I am Pavan teja, I invite you this party'
print(f'Hii ra {guests[0].title()} {message}')
print(f'Hii ra {guests[1].title()} {message}')
print(f'Hii ra {guests[2].title()} {message}')
print(f'Hii ra {guests[3].title()} {message}')
print(f'\noh! {guests[3].title()} could not make it as it is lockdown and he is far away in bihar')
guests[3] = 'advaith'
print('so now the new invitations would be like: ')
print(f'\tHii ra {guests[0].title()} {message}')
print(f'\tHii ra {guests[1].title()} {message}')
print(f'\tHii ra {guests[2].title()} {message}')
print(f'\tHii ra {guests[3].title()} {message}')
