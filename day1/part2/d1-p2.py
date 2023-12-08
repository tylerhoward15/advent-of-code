word_bank = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def get_first_num(txt):
    for i in range(len(txt)):
        res = get_number(txt, i)
        if res is not None:
            return res
            

        
def get_last_num(txt):
    for i in range(len(txt)):
        res = get_number(txt, len(txt)-1-i)
        if res is not None:
            return res

def get_number(txt, index):
    if txt[index].isdigit():
        return txt[index]
    
    for word, digit in word_bank.items():
        new_end = index + len(word)
        if (new_end) <= len(txt):
            if txt[index:new_end] == word:
                return digit
    return None


# print(get_number('oneasdf', 0) == True)
# print(get_number('oneasdf', 1) == False)
# print(get_number('fafasfweoneasdf', 1) == False)
# print(get_number('fafasfweoneasdf', 8) == True)



f = open("input.txt", "r")
sum = 0
for line in f:
    strun = str(get_first_num(line)) + str(get_last_num(line))
    # print(strun)
    # if sum > 10:
    #     break
    # else:
    #     sum += 1
    sum += int(strun)

print(f'The sum is {sum}')


f.close()