from random import choice
from random import randint

print('Enter 1 to know about Game',
      'Enter 2 to start the Game', sep='\n')

cmd = input('> ')
if cmd == '1':
    print('\nThis Program is a simulation of lottery',
          'you can assume you are having lottery tickets alphabet value(A-Z) of your wish',
          'or Numbered values(1 to 1000) of your wish',
          'Program takes your inputs and then randomly chooses 4 tickets from Alphabet and numbers from 1 to 1000',
          'And it displays whether your ticket is in the winner tickets....\n', sep='\n')

if cmd == '2':
    pass

while True:
    try:
        count_num = int(input('\nplease enter no.of number tickets you are having: '))
        count_alph = int(input('please enter no.of alphabet tickets you are having: '))

        tickets = []

        # To take the int input as many times the user is having numbered tickets
        for i in range(1, count_num + 1):
            tickets_num = int(input('please enter the values of numbered tickets you are having in order: '))
            tickets.append(tickets_num)

        # To take the alphabetical input as many times the user is having alphabet tickets
        for h in range(1, count_alph + 1):
            tickets_alph = input('please enter the alphabet tickets you are having: ')
            tickets.append(tickets_alph.title())

        lotr_num = []  # To store the list of numbers for lottery
        for i in range(1, 11):
            num = randint(1, 1000)
            lotr_num.append(num)

        lotr_alph = []  # To store the list of alphabets for lottery
        alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                     'v', 'w', 'x', 'y', 'z']
        for i in range(1, 6):
            alph = choice(alphabets)
            lotr_alph.append(alph.title())

        lotr_semis = []

        for alphs in lotr_alph:
            lotr_semis.append(alphs)

        for num in lotr_num:
            lotr_semis.append(num)

        lotr_final = []
        for l in range(1, 5):
            value = choice(lotr_semis)
            lotr_final.append(value)

        print('\nFollowing are the tickets you are Having: ')
        for ticket in tickets:
            print(f"\t\t\t\t\t\t\t\t\t{ticket}")


        print("Any ticket Matching the following Numbers or Alphabets will get a gift: ")
        for lotrwinner_value in lotr_final:
            print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t-->{lotrwinner_value}")

        len_unmatched = []

        for value in lotr_final:
            if value in tickets:
                print('one of the tickets matched! congrats!!')
                print(f'matched value is {value}')
            else:
                len_unmatched.append(value)

        if len(len_unmatched) == 4:
            print('Sorry none of your tickets are matched with winning tickets\nBetter luck next time...')
        break

    except ValueError:
        print('\nplease enter a Valid Input.. i.e, enter a number for numbered tickets and alphabets for alphabet tickets...')

