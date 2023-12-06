def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    
    # LOGIC 1
    times = [int(num) for num in lines[0][5:].split(" ") if num]
    distances = [int(num) for num in lines[1][9:].split(" ") if num]

    total1 = 1
    for i in range(4):
        time = times[i]
        distance = distances[i]
        winners = []
        for j in range(1, time):
            if (time-j)*j > distance:
                winners.append((time-j)*j)
        total1 *= len(winners)

    print(f"First answer: {total1}")

    # LOGIC 2
    times = [num for num in lines[0][5:].split(" ") if num]
    distances = [num for num in lines[1][9:].split(" ") if num]
    
    time_str = ""
    distance_str = ""
    for t in times:
        time_str = time_str + t
    for d in distances:
        distance_str = distance_str + d
    time = int(time_str)
    distance = int(distance_str)

    winners = []
    for i in range(1, time):
        if (time-i)*i > distance:
            winners.append((time-i)*i)

    print(f"Second answer: {len(winners)}")

main()
