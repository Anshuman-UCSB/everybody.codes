def part1(inp):
    mapping = {"A": 0, "B": 1, "C": 3}
    return sum(mapping[c] for c in inp)


def part2(inp, group_size=2):
    mapping = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}

    ans = 0
    for i in range(0, len(inp), group_size):
        sub = inp[i : i + group_size]
        mobs = len(sub) - sub.count("x")
        pot = sum(mapping[c] for c in sub)
        if mobs == 2:
            pot += group_size - 1
        if mobs == 3:
            pot += 3 * (group_size - 1)
        ans += pot
    return ans


if __name__ == "__main__":
    import sys

    inp = sys.stdin.read()
    # print("Part 1:",part1(inp))
    # print("Part 2:", part2(inp))
    print("Part 3:", part2(inp, group_size=3))
