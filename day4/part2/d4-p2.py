import re


winning_nums_pattern = re.compile(r"[\ \d]+\ \|")
my_nums_pattern = re.compile(r"\|[\ \d]+")
card_num_pattern = re.compile(r"Card[\s]+[\d]+")

def count_wins(winning, played):
    count = 0
    for num in played:
        if num in winning:
            count += 1
    return count


f = open("input.txt", "r")

cards = {} # k: number, v: {cards}
highest_card = 0

for line in f:
    card_num = int(re.search(card_num_pattern, line).group().replace('Card', '').strip())
    my_nums = re.search(my_nums_pattern, line).group().replace('|', '').strip().split(' ')
    my_nums = [int(x) for x in my_nums if x != '']
    winning_nums =  re.search(winning_nums_pattern, line).group().replace('|', '').strip().split(' ')
    winning_nums = [int(x) for x in winning_nums if x != '']
    occurences = 1
    
    cards[card_num] = {
        'my_nums': my_nums,
        'winning_nums': winning_nums,
        'occurences': occurences
    }
    
    if card_num > highest_card:
        highest_card = card_num


for number, card in cards.items():
    win_count = count_wins(card['winning_nums'], card['my_nums'], card['occurences'])
    for x in range(win_count):
        new_i = int(number) + x + 1
        if new_i <= highest_card:
            for _ in range(card['occurences']):
                cards[new_i]['occurences'] += 1


count = 0
for card in cards.values():
    count += card['occurences']
print(f'The count is {count}')


f.close()

