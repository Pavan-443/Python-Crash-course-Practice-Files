from random import choice
from random import randint

count_num = int(input('please enter no.of number tickets you are having: '))
count_alph = int(input('please enter no.of alphabet tickets you are having: '))

tickets = []

for i in range(1, count_num+1):
    tickets_num = int(input('please enter the numbered tickets you are having: '))
    tickets.append(tickets_num)

for h in range(1, count_alph+1):
    tickets_alph = input('please enter the alphabet tickets you are having: ')
    tickets.append(tickets_alph.title())


n = 0
x = 1
while x != 0:
    n += 1
    lotr_num = []
    for i in range(1,11):
        num = randint(1,1000)
        lotr_num.append(num)

    lotr_alph = []
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(1,6):
        alph = choice(alphabets)
        lotr_alph.append(alph.title())

    lotr_semis = []

    for alphs in lotr_alph:
        lotr_semis.append(alphs)

    for num in lotr_num:
        lotr_semis.append(num)

    lotr_final = []
    for l in range(1,5):
        value = choice(lotr_semis)
        lotr_final.append(value)

    print("Any ticket Matching the following Numbers or Alphabets: ")
    for lotrwinner_value in lotr_final:
        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t-->{lotrwinner_value}")


    for value in lotr_final:
        if value not in tickets:
            pass

        if value in tickets:
            print('One of the Tickets have matched')
            print(f'loop processed for {n} times')
            x = 0