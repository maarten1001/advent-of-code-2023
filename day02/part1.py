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
    limit = {
        "red":   12,
        "green": 13,
        "blue":  14
    }
    games = process_input()
    for i, game in enumerate(games):
        possible = True
        j = 0
        while possible and j < len(game):
            cubes = game[j].split(",")
            for cube in cubes:
                amount, colour = cube.split()
                amount = int(amount.strip())
                colour = colour.strip()
                if amount > limit[colour]:
                    possible = False
                    break
            j += 1
        if possible is True:
            print(f"Game {i + 1} would be possible")
            total += i + 1
        else:
            print(f"Game {i + 1} would not be possible")

    print(total)


if __name__ == "__main__":
    solve()
