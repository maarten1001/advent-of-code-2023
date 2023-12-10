def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        return entries


def solve():
    total = 0
    lines = process_input()
    for i, line in enumerate(lines):
        first = last = None
        for char in line:
            if char.isdecimal():
                if first is None:
                    first = char
                last = char
        value = first + last
        # print(f"The calibration value for line {i} is {value}")
        total += int(value)
    print(total)


if __name__ == "__main__":
    solve()
