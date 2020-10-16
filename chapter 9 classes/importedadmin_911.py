import privileges
pavan = privileges.Admin('paavan', 'teja', 17, 'markapur')
pavan.privilege.privileges = 'can chat', 'can edit'
pavan.privilege.show_privileges()
