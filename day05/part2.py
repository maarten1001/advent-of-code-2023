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


def solve():
    current_numbers, maps = process_input()
    for k, v in maps.items():
        new_numbers = []
        while len(current_numbers) > 0:
            number_start = current_numbers.pop(0)
            number_length = current_numbers.pop(0)
            number_end = number_start + number_length - 1
            unmapped = True

            for line in v["content"]:
                destination_start, source_start, range_length = line
                source_end = source_start + range_length - 1
                diff = destination_start - source_start

                if number_start in range(source_start, source_end + 1):
                    if number_end in range(source_start, source_end + 1):
                        # number_start is in the map and number_end is in the map
                        new_start = number_start + diff
                        new_length = number_length
                        new_numbers.extend([new_start, new_length])
                        unmapped = False
                        break
                    else:
                        # number_start is in the map, number_end is not in the map
                        new_start = number_start + diff
                        new_length = source_end - number_start + 1
                        new_numbers.extend([new_start, new_length])

                        number_start += new_length
                        number_length -= new_length
                        current_numbers.extend([number_start, number_length])
                        unmapped = False
                        break
                else:
                    if number_end in range(source_start, source_end + 1):
                        # number_start is not in the map, number_end is in the map
                        new_start = source_start + diff
                        new_length = number_end - source_start + 1
                        new_numbers.extend([new_start, new_length])

                        number_length -= new_length
                        current_numbers.extend([number_start, number_length])
                        unmapped = False
                        break
                    else:
                        # number_start and number_end are not in the map, but part of the number range might be
                        if (source_start in range(number_start, number_end + 1) and
                                source_end in range(number_start, number_end + 1)):
                            new_start = source_start + diff
                            new_length = range_length
                            new_numbers.extend([new_start, new_length])

                            number_length = source_start - number_start
                            current_numbers.extend([number_start, number_length])

                            number_start = source_end + 1
                            number_length = number_end - number_start + 1
                            current_numbers.extend([number_start, number_length])
                            unmapped = False
                            break
                        else:
                            # no overlap
                            pass
            if unmapped is True:
                new_numbers.extend([number_start, number_length])

        current_numbers = new_numbers.copy()

    locations = current_numbers[::2]
    print(min(locations))


if __name__ == "__main__":
    solve()
