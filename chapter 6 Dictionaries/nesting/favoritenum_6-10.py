fav_numinfo = {
        'jayakar': [1,2,3,4,5],
        'advaith': [6,7,8,9],
        'pavan' : [10,11,12],
        'rudheer': [13,14],
        'varshith': [15]
	}
for name, fav_num in fav_numinfo.items():
    if len(fav_num) == 1:
        print(f"\nfavorite number of {name} is {fav_num}")
    if len(fav_num) >1:
        print(f'\nfavourite numbers of {name} are: {fav_num[:]} ')