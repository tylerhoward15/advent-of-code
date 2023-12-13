import re


f = open("../input.txt", "r")
txt = f.read()
f.close()

times = [59707878]
distances = [430121812131276]

races = []
number_of_wins = []
memo = {}

def can_win(speed, time, distance) -> bool:
    key = (speed, time, distance)
    if key in memo:
        return memo[key]
    elif speed * time > distance:
            memo[key] = True
            return True
    
    memo[key] = False
    return False


def find_first_win(time_alloted, distance_to_beat, is_reversed) -> int:
    input = reversed(range(1, time_alloted)) if is_reversed else range(1, time_alloted)

    for speed in input:
        time = time_alloted-speed
        if can_win(speed, time, distance_to_beat):
            return speed
    return -1


def populate_races():
    for x in range(len(times)):
        races.append((times[x], distances[x]))

def main():
    populate_races()

    for race in races:
        time = int(race[0])
        distance = int(race[1])
        lowest = find_first_win(time, distance, False)
        highest = find_first_win(time, distance, True)
        number_of_wins.append(highest-lowest+1)

    product = 1
    for x in number_of_wins:
        product *= x

    print(f'Number of wins for each race: {number_of_wins}')
    print(f'The total of all the wins multiplied by each other: {product}')


if __name__ == '__main__':
    main()

# find the lowest time to win
# find the highest time to win
# the nums of way to win for that race is high-low+1

# multiply all nums of way to win