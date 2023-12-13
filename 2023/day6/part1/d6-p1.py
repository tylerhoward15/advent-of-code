import re


times_pattern = re.compile(r"Time:\ [\d\ ]+")
distances_pattern = re.compile(r"Distance:\ [\d\ ]+")


f = open("test.txt", "r")
txt = f.read()
f.close()

times = re.search(times_pattern, txt).group().replace('Time:','')
times = re.sub(r'[\ ]+', r' ', times).strip().split(' ')

distances = re.search(distances_pattern, txt).group().replace('Distance:','')
distances = re.sub(r'[\ ]+', r' ', distances).strip().split(' ')
races = []

for x in range(len(times)):
    races.append((times[x], distances[x]))

for race in races:
    time = int(race[0])
    distance = int(race[1])

    print(time, distance)

