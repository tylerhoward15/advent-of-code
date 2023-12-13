import re
import sys


seeds_pattern = re.compile(r"seeds: ([\d\ ]+)")
seed_to_soil_pattern = re.compile(r"seed-to-soil\ map:\n([\d\ \n]+)")
soil_to_fertilizer_pattern = re.compile(r"soil-to-fertilizer\ map:\n([\d\ \n]+)")
fertilizer_to_water_pattern = re.compile(r"fertilizer-to-water\ map:\n([\d\ \n]+)")
water_to_light_pattern = re.compile(r"water-to-light\ map:\n([\d\ \n]+)")
light_to_temperature_pattern = re.compile(r"light-to-temperature\ map:\n([\d\ \n]+)")
temperature_to_humidity_pattern = re.compile(r"temperature-to-humidity\ map:\n([\d\ \n]+)")
humidity_to_location_pattern = re.compile(r"humidity-to-location\ map:\n([\d\ \n]+)")


f = open("test.txt", "r")
txt = f.read()
f.close()


def transform_with_pattern(seed, pattern):
    match = re.findall(pattern, txt)[0]
    transformations = match.strip().split('\n')

    for transform in transformations:
        splt = transform.split(' ')

        dest = int(splt[0])
        src = int(splt[1])
        count = int(splt[2])

        upper_lim = src+count-1
        lower_lim = src

        if seed >= lower_lim and seed <= upper_lim:
            seed = dest + (seed-lower_lim)
            return seed

    return seed


min_location = sys.maxsize

seeds = [int(x) for x in (re.findall(seeds_pattern, txt)[0].strip().split(' '))]
fancy_seeds = []
# seeds = [14] # for testing

i = 0
while (i < len(seeds)-1):
    start = seeds[i]
    size = seeds[i+1]
    fancy_seeds.append([start, size])
    i += 2


for pair in fancy_seeds:
    start = pair[0]
    size = pair[1]

    for seed in range(start, start+size):
        current = seed

        current = transform_with_pattern(current, seed_to_soil_pattern)
        current = transform_with_pattern(current, soil_to_fertilizer_pattern)
        current = transform_with_pattern(current, fertilizer_to_water_pattern)
        current = transform_with_pattern(current, water_to_light_pattern)
        current = transform_with_pattern(current, light_to_temperature_pattern)
        current = transform_with_pattern(current, temperature_to_humidity_pattern)
        current = transform_with_pattern(current, humidity_to_location_pattern)

        if current < min_location:
            min_location = current

print(f'Min value for location: {min_location}')
