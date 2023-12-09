import re


numbers_pattern = re.compile(r"[\d]+")
symbol_pattern = re.compile(r"[^.\d\s]+")


sum = 0

f = open("input.txt", "r")
txt = f.read()

def get_row_above(index):
    return index - (get_line_size()+1)

def get_row_below(index):
    return index + (get_line_size()+1)

def get_line_size():
    return txt.find('\n')

def contains_symbol(string): # prone to errors, didn't double check
    if re.match(symbol_pattern, string):
        return True
    return False



# this checks if the three rows at start with a certain width contain any symbols
def valid_box(start, end, txt):
    middle_start = start if start == 0 else start-1
    middle_end = end if txt[end] == '\n' else end+1

    if valid_row(middle_start, middle_end, txt):
        return True
    
    top_start = get_row_above(middle_start)
    top_end = get_row_above(middle_end)

    if top_start > 0 and valid_row(top_start, top_end, txt):
        return True
    

    bottom_start = get_row_below(middle_start)
    bottom_end = get_row_below(middle_end)

    if bottom_start < len(txt) and valid_row(bottom_start, bottom_end, txt):
        return True
    
    
    return False

def valid_row(start, end, txt):
    print(f'row: {txt[start:end]}, start: {start}, end: {end}')
    match = re.search(symbol_pattern, txt[start:end])
    if match:
        return True




matches = re.finditer(numbers_pattern, txt)
for potential_part_num in matches:
    if valid_box(potential_part_num.start(), potential_part_num.end(), txt):
        sum = sum + int(potential_part_num.group())




# Need to check start - 1, end+1, then those positions for the line above, and those positions for the line below


print(f'The sum is {sum}')
             
f.close()