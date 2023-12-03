def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    array = []
    for line in lines:
        array.append(line)

    # PART 1
    total1 = 0
    for i in range(len(array)):
        for j in range(len(array[0])):
            char = array[i][j]
            if not char.isdigit() and char != "." and char != "\n":
                blacklist = []
                for k in range(-1, 2):
                    for m in range(-1, 2):
                        if array[i+k][j+m].isdigit() and not [i+k, j+m] in blacklist:
                            total1 += extractNumber(i+k, j+m, array, blacklist)

    # PART 2
    total2 = 0
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == "*":
                storage = []
                blacklist = []
                for k in range(-1, 2):
                    for m in range(-1, 2):
                        if array[i+k][j+m].isdigit() and not [i+k, j+m] in blacklist:
                            storage.append(extractNumber(i+k, j+m, array, blacklist))
                if len(storage) == 2:
                    total2 += storage[0] * storage[1]

    # PRINT
    print(f"First answer {total1}")
    print(f"Second answer {total2}")

def extractNumber(i, j, array, blacklist):
    number = ""
    while j-1 >= 0 and array[i][j-1].isdigit():
        j = j-1
    while array[i][j].isdigit():
        blacklist.append([i, j])
        number = number + array[i][j]
        j += 1
    return int(number)

main()
