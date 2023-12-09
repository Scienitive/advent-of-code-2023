def main():
    file = open("input.txt", "r")
    lines = file.readlines()

    total1 = 0
    total2 = 0
    for line in lines:
        numbers = [[int(num) for num in line.split(" ")]]
        i = 0
        while True:
            numbers.append([])
            for j in range(1, len(numbers[i])):
                numbers[i+1].append(numbers[i][j] - numbers[i][j-1])
            if numbers[i+1].count(0) == len(numbers[i+1]):
                break
            i += 1
        # LOGIC 1
        numbers[-1].append(0)
        for i in reversed(range(len(numbers)-1)):
            numbers[i].append(numbers[i][-1] + numbers[i+1][-1])
        total1 += numbers[0][-1]

        # LOGIC 2
        numbers[-1].insert(0, 0)
        for i in reversed(range(len(numbers)-1)):
            numbers[i].insert(0, numbers[i][0] - numbers[i+1][0])
        total2 += numbers[0][0]

    # PRINT
    print(f"First answer: {total1}")
    print(f"Second answer: {total2}")

        

main()
