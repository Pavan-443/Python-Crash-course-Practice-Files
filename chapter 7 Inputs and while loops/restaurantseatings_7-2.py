prompt = 'Hii! How many no.of of people are there in your dinner group??'
prompt+= '\nso that i can check whether there is a ready table: '
seating_num = int(input(prompt))
if seating_num <= 8:
    print('\nYour Table is Ready!!')
else:
    print('\nPlease wait for a while. we are getting your table ready.'
          '\nsorry for any delay caused')