import sys
sys.setrecursionlimit(40000)

def main():
    file = open("input.txt", "r")
    lines = file.readlines()

    pipes = {
        "7": (0, 1),
        "J": (0, 2),
        "-": (0, 3),
        "|": (1, 2),
        "F": (1, 3),
        "L": (2, 3),
        "S": (0, 1, 2, 3),
    }
    pipes_expand = {
        "7": [
            [0, 0, 0],
            [1, 1 ,0],
            [0, 1, 0],
        ],
        "J": [
            [0, 1, 0],
            [1, 1 ,0],
            [0, 0, 0],
        ],
        "-": [
            [0, 0, 0],
            [1, 1 ,1],
            [0, 0, 0],
        ],
        "|": [
            [0, 1, 0],
            [0, 1 ,0],
            [0, 1, 0],
        ],
        "F": [
            [0, 0, 0],
            [0, 1 ,1],
            [0, 1, 0],
        ],
        "L": [
            [0, 1, 0],
            [0, 1 ,1],
            [0, 0, 0],
        ],
        "S": [
            [1, 1, 1],
            [1, 1 ,1],
            [1, 1, 1],
        ],
    }
    i, j = find_start(lines)
    loop = []

    # LOGIC 1
    dir = initialize_dir(pipes, lines, i, j)
    count = 0
    while True:
        tupl = dir_to_tuple(dir)
        i += tupl[0]
        j += tupl[1]
        count += 1
        loop.append((i, j))
        if lines[i][j] == "S":
            break
        dir = pipes[lines[i][j]][0] if pipes[lines[i][j]][0] != 3-dir else pipes[lines[i][j]][1]

    # LOGIC 2
    expanded_loop = [[0] * (len(lines[0]) * 3) for _ in range(len(lines) * 3)]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if (i, j) in loop:
                for k in range(3):
                    for m in range(3):
                        expanded_loop[i*3+k][j*3+m] = pipes_expand[lines[i][j]][k][m]

    fill(expanded_loop, 0, 0)

    total2 = 0
    for i in range(0, len(expanded_loop), 3):
        for j in range(0, len(expanded_loop[0]), 3):
            found = True
            for k in range(3):
                for m in range(3):
                    if expanded_loop[i+k][j+m] != 0:
                        found = False
                        break
                if not found:
                    break
            if found:
                total2 += 1

    # COOL VISUALIZATION   
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if (i, j) in loop:
                if lines[i][j] == "L":
                    print("└", end="")
                elif lines[i][j] == "J":
                    print("┘", end="")
                elif lines[i][j] == "7":
                    print("┐", end="")
                elif lines[i][j] == "F":
                    print("┌", end="")
                elif lines[i][j] == "-":
                    print("─", end="")
                elif lines[i][j] == "|":
                    print("│", end="")
                else:
                    print("O", end="")
            else:
                print(".", end="")
        print("")

    # PRINT
    print(f"First answer: {count//2}")
    print(f"Second answer: {total2}")

def fill(array, x, y):
    if x < 0 or x >= len(array) or y < 0 or y >= len(array[0]) or array[x][y] != 0:
        return
    array[x][y] = 2
    fill(array, x+1, y)
    fill(array, x-1, y)
    fill(array, x, y+1)
    fill(array, x, y-1)
    
def find_start(lines):
    for i, line in enumerate(lines):
        if "S" in line:
            return i, line.index("S")
    return 0, 0

def initialize_dir(pipes, lines, i, j):
    if 0 in pipes[lines[i][j+1]]:
        return 3
    elif 3 in pipes[lines[i][j-1]]:
        return 0
    elif 1 in pipes[lines[i-1][j]]:
        return 2
    elif 2 in pipes[lines[i+1][j]]:
        return 1
    return -1

def dir_to_tuple(dir):
    if dir == 0:
        return (0, -1)
    elif dir == 1:
        return (1, 0)
    elif dir == 2:
        return (-1, 0)
    elif dir == 3:
        return (0, 1)
    return (0, 0)



main()
