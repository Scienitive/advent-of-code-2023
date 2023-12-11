def main():
    file = open("input.txt", "r")
    lines = file.readlines()

    empty_rows = []
    empty_cols = []

    # EMPTY SPACE DETECTING
    for i in range(len(lines)):
        if lines[i].count(".") == len(lines[i])-1:
            empty_rows.append(i)

    for i in range(len(lines[0])-1):
        ok = True
        for j in range(len(lines)):
            if lines[j][i] != ".":
                ok = False
                break
        if ok:
            empty_cols.append(i)

    # GALAXY POSITIONS
    positions = []
    for i in range(len(lines)):
        for j in range(len(lines[0])-1):
            if lines[i][j] == "#":
                positions.append((i, j))

    # LOGIC 1 AND LOGIC 2
    total1 = 0
    total2 = 0
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            total1 += find_path(positions[i], positions[j], empty_rows, empty_cols, 2)
            total2 += find_path(positions[i], positions[j], empty_rows, empty_cols, 1000000)

    # PRINT
    print(f"First answer: {total1}")
    print(f"Second answer: {total2}")

def insert_char(string, char, pos):
    return string[:pos] + char + string[pos:]

def find_path(pos1, pos2, empty_rows, empty_cols, dist):
    empty_space = 0
    for index in empty_cols:
        if (index > pos1[1] and index < pos2[1]) or (index < pos1[1] and index > pos2[1]):
            empty_space += dist-1
    for index in empty_rows:
        if (index > pos1[0] and index < pos2[0]) or (index < pos1[0] and index > pos2[0]):
            empty_space += dist-1
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) + empty_space

main()
