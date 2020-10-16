#I am T.Pavan teja
#Date is 3rd August,2020.
invitees = ['jayakar', 'rudheer', 'varshith', 'vikash']
message = 'I am inviting you to this party'

for invitee in invitees:
	print(f'\tHii ra {invitee}, {message}')
print(f'so now I an inviting {len(invitees)} people to the party')

print(f'\noh! {invitees[3].title()} could not make it to this party as it is lockdown and he is far away in bihar')
invitees[3] = 'advaith'

print('\nso now the new invitations would be like: ')
for invitee in invitees:
	print(f'\tHii ra {invitee}, {message}')
print(f'so now i am inviting {len(invitees)} people to the party')

print(f'\nWow! it is amazing I have found a bigger dining table, so now I can call more people to this party.....')
invitees.insert(0, 'dheeraj')
invitees.insert(2, 'charan sai')
invitees.append('harshil')

print('so now the new invitations would be like: ')
for invitee in invitees:
	print(f'\tHii ra {invitee}, {message}')
print(f'so now i am inviting {len(invitees)} people to the party')

print('\noh! I thought I will get the big table on time but the delivery is delayed due to some issue, now I can only invite two people...')
reason = 'I cannot invite you to this Party...., because I thought I will get the big table on time but the delivery is delayed due to some issue, now I can only invite two people... I hope you will understand this'

popped_invitee1 = invitees.pop()
print(f'\n\tsorry ra {popped_invitee1.title()} {reason}') #print the sorry message....
print(f'so now i am inviting {len(invitees)} people to the party')
popped_invitee2 = invitees.pop()
print(f'\n\tsorry ra {popped_invitee2.title()} {reason}')
print(f'so now i am inviting {len(invitees)} people to the party')
popped_invitee3 = invitees.pop()
print(f'\n\tsorry ra {popped_invitee3.title()} {reason}')
print(f'so now i am inviting {len(invitees)} people to the party')
popped_invitee4 = invitees.pop()
print(f'\n\tsorry ra {popped_invitee4.title()} {reason}')
print(f'so now i am inviting {len(invitees)} people to the party')
popped_invitee5 = invitees.pop()
print(f'\n\tsorry ra {popped_invitee5.title()} {reason}')
print(f'so now i am inviting {len(invitees)} people to the party')

print('\nso now the new invitations would be like: ')
print(f'\t\tHii ra {invitees[0].title()} {message}')
print(f'\t\tHii ra {invitees[1].title()} {message}')
print(f'so now i am inviting {len(invitees)} people to the party')

del invitees[0]
del invitees[0]
print(f'Now the invitees are {invitees}')

print(f'so now i am inviting {len(invitees)} people to the party')
