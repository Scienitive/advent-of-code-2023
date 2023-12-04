def main():
    file = open("input.txt", "r")
    lines = file.readlines()

    # LOGIC 1
    total1 = 0
    for line in lines:
        col_index = line.find(":")
        bar_index = line.find("|")
        winners = [int(num) for num in line[col_index+2:bar_index-1].split(" ") if num]
        my_cards = [int(num) for num in line[bar_index+2:-1].split(" ") if num]

        points = 0
        for winner in winners:
            if winner in my_cards:
                points = 1 if points == 0 else points * 2
        total1 += points

    # LOGIC 2
    total2 = 0
    array = [1] * 203
    for i, line in enumerate(lines):
        col_index = line.find(":")
        bar_index = line.find("|")
        winners = [int(num) for num in line[col_index+2:bar_index-1].split(" ") if num]
        my_cards = [int(num) for num in line[bar_index+2:-1].split(" ") if num]

        next = 1
        for winner in winners:
            if winner in my_cards:
                array[i+next] += array[i]
                next += 1
    for item in array:
        total2 += item

    # PRINT
    print(f"First answer: {total1}")
    print(f"Second answer: {total2}")

main()
