def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    games = []

    # TXT TO ARRAY
    for line in lines:
        colon_index = line.find(":")
        split = line[colon_index+1:].split(";")
        rgbs = []
        for string in split:
            index = 1
            rgb = [0, 0, 0]
            while index < len(string):
                num = index_to_num(string, index)
                index += place(rgb, string[index+1+len(str(num))], num)
            rgbs.append(rgb)
        games.append(rgbs)

    # LOGIC 1
    total1 = 0
    rgb_limit = [12, 13, 14]
    for i, game in enumerate(games):
        ok = True
        for rgb in game:
            if rgb[0] > rgb_limit[0] or rgb[1] > rgb_limit[1] or rgb[2] > rgb_limit[2]:
                ok = False
                break
        if ok:
            total1 += i + 1

    # LOGIC 2
    total2 = 0
    for game in games:
        game_rgb = [0, 0, 0]
        for rgb in game:
            for i in range(3):
                if game_rgb[i] == 0 or game_rgb[i] < rgb[i]:
                    game_rgb[i] = rgb[i]
        total2 += game_rgb[0] * game_rgb[1] * game_rgb[2]

    # PRINT
    print(f"First answer: {total1}")
    print(f"Second answer: {total2}")

def place(arr, char, num):
    if char == "r":
        arr[0] = num
        return 6 + len(str(num))
    elif char == "g":
        arr[1] = num
        return 8 + len(str(num))
    elif char == "b":
        arr[2] = num
        return 7 + len(str(num))
    return 0

def index_to_num(string, index):
    num = 0
    while string[index].isdigit():
        num *= 10
        num += int(string[index])
        index += 1
    return num

main()
