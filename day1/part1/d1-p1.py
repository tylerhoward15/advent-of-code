def get_first_num(str):
    for char in str:
        if char.isdigit():
            return char
        
def get_last_num(str):
    for i in range(len(str)):
        if str[len(str)-1-i].isdigit():
            return str[len(str)-1-i]



f = open("input.txt", "r")
sum = 0
for line in f:
    sum += int(str(get_first_num(line)) + str(get_last_num(line)))

print(f'The sum is {sum}')


f.close()