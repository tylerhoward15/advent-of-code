import re

pattern = re.compile(r"([\w]+)\ ([\w]+)")
players = []

def read_input():
    # f = open("../test.txt", "r")
    f = open("../input.txt", "r")

    for line in f:
        match = re.search(pattern, line)
        hand = match[1] if match else None
        bid = int(match[2]) if match else None

        player = {
            'hand': hand,
            'bid': bid,
            'score': get_total_score(hand)
        }

        players.append(player)
    f.close()

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
    freqMap = get_freq_map(hand)

    max_card, max_count = max(freqMap.items(), key=lambda x: x[1])
    if max_count == 5:
        # print(f'5 of a kind for {hand}')
        return 10**60
    if max_count == 4:
        # print(f'4 of a kind for {hand}')
        return 10**50
    
    temp = list(freqMap.values())

    if max_count == 3:
        if temp.count(2) + temp.count(3) > 1:
            # print(f'full house for {hand}')
            return 10**40
        else:
            # print(f'3 of a kind for {hand}')
            return 10**30
    if max_count == 2:
        if temp.count(2) > 1:
            # print(f'2 pair for {hand}')
            return 10**20
        # print(f'1 pair for {hand}')
        return 10**10
    # print(f'no bonus for {hand}')
    return 0

def get_base_score(hand) -> int:
    first = parse_card(hand[0]) * (14**4)
    second = parse_card(hand[1]) * (14**3)
    third = parse_card(hand[2]) * (14**2)
    fourth = parse_card(hand[3]) * (14**1)
    fifth = parse_card(hand[4]) * (14**0)

    return first + second + third + fourth + fifth


def parse_card(char) -> int:
    if char == 'A':
        return 14
    if char == 'K':
        return 13
    if char == 'Q':
        return 12
    if char == 'J':
        return 11
    if char == 'T':
        return 10
    return int(char)


def main():
    assert(get_base_score('AAAKA') < get_base_score('AAAA2'))
    read_input()

    score_sort = sorted(players, key=lambda player: player['score'])
    rovs = [player['bid']*(i+1) for i, player in enumerate(score_sort)]

    sum = 0
    for x in rovs:
        sum += x

    print(f'sum of rovs: {sum}')
    return

def test():
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
