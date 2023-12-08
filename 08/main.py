import math

def main():
    file = open("input.txt", "r")
    lines = file.readlines()

    # LOGIC 1
    j = 0
    i = 0
    name = "AAA"
    while name != "ZZZ":
        if i >= len(lines[0])-1:
            i = 0
        name = find_way(name, lines[0][i], lines)
        i += 1
        j += 1

    print(f"First answer: {j}")

    # LOGIC 2
    numbers = []
    for line in lines:
        if len(line) > 3 and line[2] == "A":
            numbers.append(get_loop_info(line[:3], lines))

    print(f"Second answer: {math.lcm(*numbers)}")

def get_loop_info(name, lines):
    stops = [[name, 0]]
    loop_start_index = 0
    i = 0
    while True:
        if i >= len(lines[0])-1:
            i = 0
        name = find_way(name, lines[0][i], lines)
        obj = [name, i]
        if obj in stops:
            loop_start_index = stops.index(obj)
            break
        stops.append(obj)
        i += 1
    return len(stops) - loop_start_index

def find_way(name, dir, lines):
    for line in lines[2:]:
        if line[:3] != name:
            continue
        if dir == "L":
            return line[7:10]
        elif dir == "R":
            return line[12:15]

main()
