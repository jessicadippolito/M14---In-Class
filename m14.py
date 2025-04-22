import os
my_file = open('contest.txt')
for line in my_file:
    print(f'{line.split(',')[0]} caught pakuri with the following levels: ', end = '')
    for i in range (1,len(line.split('-'))-1):
        print(f'{line.split("-")[i][0]}, ', end = '')
    print(f'{line.split("-")[(len(line.split('-')))-1]}', end = '')
print()
winner = ''
print(f'Since {winner} caught the highest level pakuri, {winner} is the winner.')

