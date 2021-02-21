import random

lottery_numbers = set(random.sample(range(22), 6))

players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

winner = players[0]

for player in players:
	numbers_matched = len(player['numbers'].intersection(lottery_numbers))
	if numbers_matched > len(winner['numbers'].intersection(lottery_numbers)):
			winner = player
