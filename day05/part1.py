def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        seeds = entries[0].split(":")[1].split()
        seeds = [int(x) for x in seeds]
        maps = dict()
        for i in range(2, len(entries)):
            if "map" in entries[i]:
                name = entries[i].split()[0]
                maps[name] = {
                    "source": name.split("-to-")[0],
                    "destination": name.split("-to-")[1],
                    "content": []
                }
            elif entries[i] != "":
                content = entries[i].split()
                content = [int(x) for x in content]
                maps[name]["content"].append(content)
        return seeds, maps


def mapper(m, source):
    for line in m["content"]:
        destination_start, source_start, length = line
        if source in range(source_start, source_start + length + 1):
            destination = source + (destination_start - source_start)
            return destination
    return source


def solve():
    lowest_location = float("inf")
    seeds, maps = process_input()
    for seed in seeds:
        for k, v in maps.items():
            seed = mapper(v, seed)
        if seed < lowest_location:
            lowest_location = seed
    print(lowest_location)


if __name__ == "__main__":
    solve()
