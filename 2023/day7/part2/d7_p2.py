import re

pattern = re.compile(r"([\w]+)\ ([\w]+)")
players = []

def read_input() -> None:
    with open("../test.txt", "r", encoding="utf-8") as f:
        for line in f:
            match = re.search(pattern, line)
            hand = match[1] if match else 'None'
            bid = int(match[2]) if match else 'None'

            player = {
                'hand': hand,
                'bid': bid,
                'score': get_total_score(hand)
            }

            players.append(player)

def get_freq_map(hand) -> dict:
    freq = {}
    for char in hand:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def get_total_score(hand) -> int:
    return get_base_score(hand) + get_bonus_score(hand)

def get_bonus_score(hand) -> int:
    base_bonus = 15**5 # this is due to base-15 scoring

    if hand == 'JJJJJ': 
        return base_bonus**6

    freq_map = get_freq_map(hand)
    joker_count = freq_map['J'] if 'J' in freq_map else 0

    for k in freq_map:
        if k != 'J':
            freq_map[k] += joker_count
    
    vals = [card[1] for card in freq_map.items()]
    max_count = max(vals) if vals else 0

    if max_count == 5:
        print(f'5 of a kind for hand {hand}')
        return base_bonus**6
    if max_count == 4:
        print(f'4 of a kind for hand {hand}')
        return base_bonus**5
    
    temp = list(freq_map.values())







    # THIS IS WHERE THE ISSUE IS

    if max_count == 3:
        
        if temp.count(2) + temp.count(3) > 1:
            print(f'full house for hand {hand}')
            return base_bonus**4
        else:
            print(f'3 of a kind for hand {hand}')
            return base_bonus**3
        




    if max_count == 2:
        if temp.count(2) > 1:
            print(f'2 pair for hand {hand}')
            return base_bonus**2
        print(f'1 pair for hand {hand}')
        return base_bonus**1
    print(f'no bonus for hand {hand}')
    return 0

def get_base_score(hand) -> int:
    first = parse_card(hand[0]) * (15**4)
    second = parse_card(hand[1]) * (15**3)
    third = parse_card(hand[2]) * (15**2)
    fourth = parse_card(hand[3]) * (15**1)
    fifth = parse_card(hand[4]) * (15**0)

    return first + second + third + fourth + fifth


def parse_card(char) -> int:
    if char == 'A':
        return 14
    if char == 'K':
        return 13
    if char == 'Q':
        return 12
    if char == 'T':
        return 10
    if char == 'J':
        return 1
    return int(char)


def main() -> None:
    assert(get_base_score('AAAKA') < get_base_score('AAAA2'))
    read_input()

    score_sort = sorted(players, key=lambda player: player['score'])
    rovs = [player['bid']*(i+1) for i, player in enumerate(score_sort)]

    curr_sum = 0
    for x in rovs:
        curr_sum += x

    print(f'sum of rovs: {curr_sum}')

    return

def test() -> None:
    first = 10**6 + get_base_score('32T3K') 
    second = 10**18 + get_base_score('T55J5') 
    third = 10*12 + get_base_score('KK677')
    fourth = 10*12 + get_base_score('KTJJT')
    fifth = 10*18 + get_base_score('QQQJA')

    cards = [
        first,
        second,
        third,
        fourth,
        fifth
    ]

    for card in cards:
        print(f'Score: {card:_}')


if __name__ == '__main__':
    main()
    # test()


# rank the hands from strongest to weakest
# multiply bid by rank to get a rov
# add all rov's to get answer
