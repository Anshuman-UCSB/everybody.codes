def part1(inp):
    words, _, sentence = inp.splitlines()
    words = words[6:].split(",")

    return sum(sentence.count(w) for w in words)


def part2(inp):
    words, _, *sentence = inp.splitlines()
    words = words[6:].split(",")

    def solve_line(line):
        used = [False for _ in line]
        for word in words:
            for i in range(len(line) - len(word) + 1):
                for j in range(len(word)):
                    if line[i + j] != word[j]:
                        break
                else:
                    for j in range(len(word)):
                        used[i + j] = True
        return used

    ans = 0
    for line in sentence:
        forward = solve_line(line)
        rev = solve_line(line[::-1])
        count = 0
        for i in range(len(forward)):
            if forward[i] or rev[-i - 1]:
                count += 1
        # print(line, count)
        ans += count

    return ans


def part3(inp):
    words, _, *sentence = inp.splitlines()
    words = words[6:].split(",")
    used = [[False] * len(sentence[0]) for _ in range(len(sentence))]

    def wrapcoord(x, y):
        return x % len(used[0]), y % len(used)

    for y in range(len(used)):
        for x in range(len(used[0])):
            for word in words:
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ...


if __name__ == "__main__":
    import sys

    TEST_FLAG = "test" in map(lambda x: x.lower(), sys.argv)
    FILENAME = "example" if TEST_FLAG else "part"

    def open_and_read(part):
        with open(f"{FILENAME}{part}.txt", "r") as f:
            return f.read()

    print("Part 1:", part1(open_and_read(1)))
    print("Part 2:", part2(open_and_read(2)))
    print("Part 3:", part3(open_and_read(3)))
