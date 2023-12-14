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


def solve():
    total = 0
    schematic = process_input()
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
                total += int(number)
            x += 1
    print(total)


if __name__ == "__main__":
    solve()
