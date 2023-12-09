import re

numbers_pattern = re.compile(r"[\d]+")
symbol_pattern = re.compile(r"[^.\d\s]+")
gear_pattern = re.compile(r"[*]+")


def get_row_above(index):
    return index - (get_line_size()+1)

def get_row_below(index):
    return index + (get_line_size()+1)

def get_line_size():
    return txt.find('\n')


f = open("input.txt", "r")
txt = f.read()


class Part(object):
    def __init__(self, number, start, end):
        self.number = number
        self.start = start
        self.end = end
        self.gears = [] # this will be a set of Gears
        self.valid_part = self.initialize_validity()
        

    def __repr__(self) -> str:
        return str(self.number)
    
    def initialize_validity(self):         
        middle_start = self.start if self.start == 0 else self.start-1
        middle_end = self.end if txt[self.end] == '\n' else self.end+1

        if self.valid_row(middle_start, middle_end, txt):
            return True
        
        top_start = get_row_above(middle_start)
        top_end = get_row_above(middle_end)

        if top_start > 0 and self.valid_row(top_start, top_end, txt):
           return True
        

        bottom_start = get_row_below(middle_start)
        bottom_end = get_row_below(middle_end)

        if bottom_start < len(txt) and self.valid_row(bottom_start, bottom_end, txt):
            return True
        
        return False

    def valid_row(self, start, end, txt):
        gear_match = re.finditer(gear_pattern, txt[start:end])
        for gear in gear_match:
            all_gears[int(start + gear.start())].append(self.number)

        match = re.search(symbol_pattern, txt[start:end])
        if match:
            return True


class Gear(object):
    def __init__(self, index):
        self.index = index
        self.parts = [] # this will be a set of PartNumbers

    def __repr__(self) -> str:
        return str(self.index)

all_gears = {}
gear_match = re.finditer(gear_pattern, txt)
for gear in gear_match:
    all_gears[int(gear.start())] = []


sum = 0


matches = re.finditer(numbers_pattern, txt)
for potential_part_num in matches:
    part = Part(potential_part_num.group(), potential_part_num.start(), potential_part_num.end())

for gear, parts in all_gears.items():
    if (len(parts) > 1):
        sum += int(parts[0]) * int(parts[1])

print(f'The sum is {sum}')
             
f.close()