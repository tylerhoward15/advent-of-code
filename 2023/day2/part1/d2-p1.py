import re

limits = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def valid_game(set):
    ls = set.split(',')
    for pair in ls:
        freq = pair.strip().split(' ')
        # print(f'0: {freq[0]}\n1: {freq[1]}\n')
        if int(freq[0]) > limits[freq[1]]:
            return False
    return True


game_number_pattern = re.compile(r"Game [\d]+")
game_set_pattern = re.compile(r"[\d]+\ [\w,\ ]+", re.IGNORECASE)

sum = 0

f = open("input.txt", "r")

for line in f:
    game_number = int(re.search(game_number_pattern, line).group().replace('Game ', ''))
    game_sets = re.findall(game_set_pattern, line)
    is_valid = True

    for set in game_sets:
        if not is_valid:
            break
        if not valid_game(set):
            is_valid = False

    if is_valid:
        sum = sum + game_number

print(f'The sum is {sum}')
            
f.close()