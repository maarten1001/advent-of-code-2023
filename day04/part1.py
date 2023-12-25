def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        cards = []
        for i in range(len(entries)):
            numbers = entries[i].split(":")[1]
            cards.append(numbers.split("|"))
        return cards


def solve():
    total = 0
    cards = process_input()
    for card in cards:
        points = 0
        winning_numbers, numbers_you_have = card
        winning_numbers = winning_numbers.split()
        numbers_you_have = numbers_you_have.split()
        for number_you_have in numbers_you_have:
            if number_you_have in winning_numbers:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        total += points
    print(total)


if __name__ == "__main__":
    solve()
