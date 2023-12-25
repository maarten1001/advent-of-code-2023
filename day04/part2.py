def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        cards = []
        for i in range(len(entries)):
            numbers = entries[i].split(":")[1]
            numbers = numbers.split("|")
            card = {
                "count": 1,
                "winning_numbers": set(numbers[0].split()),
                "numbers_you_have": set(numbers[1].split())
            }
            cards.append(card)
        return cards


def solve():
    cards = process_input()
    for i, card in enumerate(cards):
        matching_numbers = card["numbers_you_have"].intersection(card["winning_numbers"])
        j = 1
        while i + j < len(cards) and j <= len(matching_numbers):
            cards[i + j]["count"] += cards[i]["count"]
            j += 1
    print(sum([i["count"] for i in cards]))


if __name__ == "__main__":
    solve()
