def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    total1 = 0
    total2 = 0

    for line in lines:
        count = 0
        buffer = 0
        first = 0
        last = 0
        for char in line:
            if char.isdigit():
                buffer = int(char)
                count += 1
                if count == 1:
                    first = buffer
        last = buffer
        total1 += (first * 10) + last
        # Second Problem
        for i, number in enumerate(numbers):
            if line.find(str(first)) == -1 and line.find(numbers[first-1]) == -1:
                if line.find(number):
                    first = i + 1
            elif line.find(number) != -1:
                if (line.find(number) < line.find(str(first)) or line.find(str(first)) == -1) and (line.find(number) < line.find(numbers[first-1]) or line.find(numbers[first-1]) == -1):
                    first = i + 1
            if line.find(str(last)) == -1 and line.find(numbers[last-1]) == -1:
                if line.rfind(number):
                    last = i + 1
            elif line.find(number) != -1:
                if line.rfind(number) > line.rfind(str(last)) and line.rfind(number) > line.rfind(numbers[last-1]):
                    last = i + 1
        total2 += (first * 10) + last

    print(f"First answer: {total1}")
    print(f"Second answer: {total2}")

main()
