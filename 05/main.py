def main():
    file = open("input.txt", "r")
    lines = file.readlines()

    # LOGIC 1
    array = [[int(num)] for num in lines[0][7:].split(" ")]

    index = 0
    for i in range(3, len(lines)):
        line = lines[i]

        if line[0] == "\n":
            continue
        if not line[0].isdigit():
            index += 1
            for item in array:
                if len(item) < index+1:
                    item.append(item[index-1])
            continue

        numbers = [int(num) for num in line.split(" ")]

        for item in array:
            if item[index] >= numbers[1] and item[index] < numbers[1] + numbers[2]:
                item.append(numbers[0] + (item[index] - numbers[1]))

    lowest = array[0][-1]
    for item in array:
        if item[-1] < lowest:
            lowest = item[-1]

    print(f"First answer: {lowest}")

    # LOGIC 2
    seeds = [int(num) for num in lines[0][7:].split(" ")]
    starting_points = [136, 115, 96, 55, 22, 3]
    order = []
    intervals = []
    index = 168
    while index < len(lines) and lines[index][0] != "\n":
        numbers = [int(num) for num in lines[index].split(" ")]
        order.append(numbers[0])
        intervals.append((numbers[1], numbers[1] + numbers[2] - 1))
        index += 1
    intervals_sorter(intervals, order)
    for i in intervals:
        the_function(i, 0, lines, starting_points, seeds)
        break

def the_function(u_interval, level, lines, starting_points, seeds):
    if level == 6:
        is_it, value = is_it_on_seeds(u_interval, seeds)
        if is_it:
            try_seed(value, lines)
        return
    index = starting_points[level]

    order = []
    intervals = []
    while index < len(lines) and lines[index][0] != "\n":
        numbers = [int(num) for num in lines[index].split(" ")]
        intersect, interval = is_intersecting(u_interval, (numbers[0], numbers[0] + numbers[2] - 1))
        if intersect:
            order.append(interval[0])
            intervals.append(dest_to_src(interval, numbers[1] - numbers[0]))
        index += 1
    cover_empty_intervals(u_interval, intervals, intervals.copy(), order)
    intervals_sorter(intervals, order)
    for i in intervals:
        the_function(i, level+1, lines, starting_points, seeds)

def dest_to_src(interval, diff):
    start, end = interval
    return (start + diff, end + diff)

def try_seed(seed, lines):
    starting_points = [3, 22, 55, 96, 115, 136, 168]
    index = 0
    while index <= 6:
        i = starting_points[index]
        while i < len(lines) and lines[i][0] != "\n":
            numbers = [int(num) for num in lines[i].split(" ")]
            if seed >= numbers[1] and seed < numbers[1] + numbers[2]:
                seed = numbers[0] + (seed - numbers[1])
                break
            i += 1
        index += 1
    print(f"Second answer: {seed}")
    exit()

def is_it_on_seeds(interval, seeds):
    for i in range(0, len(seeds), 2):
        min = seeds[i]
        max = seeds[i] + seeds[i+1] - 1
        is_it, the_interval = is_intersecting((min, max), interval)
        if is_it:
            return True, the_interval[0]
    return False, 0

def cover_empty_intervals(u_interval, r_intervals, intervals, order):
    for i, interval in enumerate(intervals):
        diff = interval[1] - interval[0]
        interval = (order[i], order[i] + diff)
        intervals[i] = interval

    i = 0
    while i < len(intervals):
        if i == 0:
            i += 1
            continue
        if intervals[i][0] < intervals[i-1][0]:
            temp = intervals[i]
            intervals[i] = intervals[i-1]
            intervals[i-1] = temp
            i -= 2
        i += 1

    big_start, big_end = u_interval
    follow = big_start
    for i in intervals:
        if i[0] != follow:
            order.append(follow)
            r_intervals.append((follow, i[0]-1))
        follow = i[1]+1
    if follow-1 != big_end:
        order.append(follow)
        r_intervals.append((follow, big_end))

def is_intersecting(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    if start1 <= end2 and start2 <= end1:
        start = max(start1, start2)
        end = min(end1, end2)
        interval = (start, end)
        return True, interval
    else:
        return False, (0, 0)

def intervals_sorter(intervals, order):
    i = 0
    while i < len(order):
        if i <= 0:
            i += 1
            continue
        if order[i] < order[i-1]:
            temp = order[i]
            order[i] = order[i-1]
            order[i-1] = temp
            temp = intervals[i]
            intervals[i] = intervals[i-1]
            intervals[i-1] = temp
            i -= 2
        i += 1

main()
