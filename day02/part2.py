def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        for i in range(len(entries)):
            record = entries[i].split(":")[1]
            entries[i] = record.split(";")
        return entries


def solve():
    total = 0
    games = process_input()
    for i, game in enumerate(games):
        maximum = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for j, cubes in enumerate(game):
            cubes = cubes.split(",")
            for cube in cubes:
                amount, colour = cube.split()
                amount = int(amount.strip())
                colour = colour.strip()
                if amount > maximum[colour]:
                    maximum[colour] = amount
        print(f'Game {i + 1} could have been played with a minimum of '
              f'{maximum["red"]} red, {maximum["green"]} green and {maximum["blue"]} blue cubes')
        total += maximum["red"] * maximum["green"] * maximum["blue"]

    print(total)


if __name__ == "__main__":
    solve()
