import re

def power_set(sets):
    maxes = {
        'green': 1,
        'blue': 1,
        'red': 1,
    }
    for game in sets:
        items = game.split(',')
        for entry in items:
            pair = entry.strip().split(' ')
            freq = int(pair[0])
            color = pair[1]
            if (maxes[color] < freq):
                maxes[color] = freq
    print(maxes)

    ret = 1
    for value in maxes.values():
       ret = ret * value 
    return ret

game_number_pattern = re.compile(r"Game [\d]+")
game_set_pattern = re.compile(r"[\d]+\ [\w,\ ]+", re.IGNORECASE)

sum = 0

f = open("input.txt", "r")

for line in f:
    game_number = int(re.search(game_number_pattern, line).group().replace('Game ', ''))
    game_sets = re.findall(game_set_pattern, line)
    sum = sum + power_set(game_sets)



print(f'The sum is {sum}')
            
f.close()