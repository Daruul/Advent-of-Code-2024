puzzle = "6571 0 5851763 526746 23 69822 9 989".split()
stones = {}
for stone in puzzle:
    stones[stone] = stones.get(stone, 0) + 1

blinks = 75
for i in range(blinks):
    newDict = {}
    for stone, count in stones.items():
        if stone == "0":
            newDict["1"] = newDict.get("1", 0) + count
        elif len(stone) % 2 == 0:
            midpoint = len(stone) // 2
            left = stone[:midpoint]
            # right = list(stone[midpoint:])
            # while right[0] == "0" and len(right) > 1:
            #     right.pop(0)
            # right = "".join(right)

            right = str(int(stone[midpoint:]))
            newDict[left] = newDict.get(left, 0) + count
            newDict[right] = newDict.get(right, 0) + count
        else:
            value = str(int(stone) * 2024)
            newDict[value] = count
    stones = newDict

    if (i == 24):
        print("Part 1:", sum(stones.values()))

print("Part 2:", sum(stones.values()))

# 203953
# 242090118578155