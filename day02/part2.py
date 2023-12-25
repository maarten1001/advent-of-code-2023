def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        games = []
        for i in range(len(entries)):
            record = entries[i].split(":")[1]
            games.append(record.split(";"))
        return games


def solve():
    total = 0
    games = process_input()
    for i, game in enumerate(games):
        minimum = {
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
                if amount > minimum[colour]:
                    minimum[colour] = amount
        print(f'Game {i + 1} could have been played with a minimum of '
              f'{minimum["red"]} red, {minimum["green"]} green and {minimum["blue"]} blue cubes')
        total += minimum["red"] * minimum["green"] * minimum["blue"]

    print(total)


if __name__ == "__main__":
    solve()
