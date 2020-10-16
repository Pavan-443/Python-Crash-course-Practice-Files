import privilege2

pavan = privilege2.Admin('ji', 'ki', 'kl', 'ko')
pavan.privilege.privileges = 'can chat', 'can cook'
pavan.privilege.show_privileges()
