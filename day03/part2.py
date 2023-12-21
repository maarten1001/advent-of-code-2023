def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        return entries


def print_grid(grid):
    for i in grid:
        for j in i:
            print(j, end='')
        print()
    print()


def is_symbol_adjacent(grid, x, y):
    for i in range(max(0, y - 1), min(len(grid), y + 2)):
        for j in range(max(0, x - 1), min(len(grid[0]), x + 2)):
            if grid[i][j] != '.' and not grid[i][j].isdecimal():
                return True
    return False


def get_gear_ratio(part_numbers, x, y):
    # we use set to remove duplicates and assume that two part numbers will never be equal
    parts = set()
    for i in range(max(0, y - 1), min(len(part_numbers), y + 2)):
        for j in range(max(0, x - 1), min(len(part_numbers[0]), x + 2)):
            if part_numbers[i][j] != 0:
                parts.add(part_numbers[i][j])
    if len(parts) != 2:
        return 0
    product = 1
    for part in parts:
        product *= part
    return product


def solve():
    total = 0
    schematic = process_input()
    part_numbers = [[0 for _ in i] for i in schematic]

    for y, line in enumerate(schematic):
        x = 0
        while x < len(line):
            number = ''
            adjacent = False
            while x < len(line) and line[x].isdecimal():
                if is_symbol_adjacent(schematic, x, y):
                    adjacent = True
                number += line[x]
                x += 1
            if adjacent is True:
                # duplicate a part number across its coordinates
                for xx in range(x - len(number), x):
                    part_numbers[y][xx] = int(number)
            x += 1

    for y, line in enumerate(schematic):
        for x in range(len(line)):
            if schematic[y][x] == '*':
                total += get_gear_ratio(part_numbers, x, y)

    print(total)


if __name__ == "__main__":
    solve()
