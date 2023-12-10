# we only use zero to keep the other numbers in their correct place
numbers = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")


def get_digit(text):
    if len(text) == 1 and text.isdecimal():
        return text
    for n in range(1, len(numbers)):
        if text == numbers[n]:
            return str(n)
    return ""


def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        return entries


def solve():
    max_length = max(len(x) for x in numbers)
    total = 0
    lines = process_input()
    for i, line in enumerate(lines):
        newline = ""
        for start in range(len(line)):
            digit = None
            for length in range(1, max_length + 1):
                if start + length > len(line):
                    break
                digit = get_digit(line[start: start + length])
                if digit != "":
                    break
            newline += digit

        if len(newline) == 0:
            raise Exception(f"Did not find a digit in line {i}")
        value = newline[0] + newline[-1]
        # print(f"The calibration value for line {i} is {value}")
        total += int(value)
    print(total)


if __name__ == "__main__":
    solve()
