import re


winning_nums_pattern = re.compile(r"[\ \d]+\ \|")
my_nums_pattern = re.compile(r"\|[\ \d]+")

def count_wins(winning, played):
    count = 0
    for num in played:
        if num in winning:
            count += 1
    return count


score = 0

f = open("input.txt", "r")
for line in f:
    my_nums = re.search(my_nums_pattern, line).group().replace('|', '').strip().split(' ')
    my_nums = [int(x) for x in my_nums if x != '']
    winning_nums =  re.search(winning_nums_pattern, line).group().replace('|', '').strip().split(' ')
    winning_nums = [int(x) for x in winning_nums if x != '']

    win_count = count_wins(winning_nums, my_nums)
    if win_count > 0:
        score += 2**(win_count-1)


print(f'The score is {score}')


f.close()

