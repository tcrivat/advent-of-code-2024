INPUT_FILE = "input.txt"

memo = {}

def evolve(stone, generation):
    if generation == 0:
        return 1
    if (stone, generation) in memo:
        return memo[(stone, generation)]
    stones = []
    if stone == "0":
        stones.append("1")
    elif len(stone) % 2 == 0:
        stones.append(stone[0 : len(stone) // 2])
        stones.append(str(int(stone[len(stone) // 2 :])))
    else:
        stones.append(str(int(stone) * 2024))
    answer = sum(evolve(stone, generation - 1) for stone in stones)
    memo[(stone, generation)] = answer
    return answer

def solution(filename):
    with open(filename) as f:
        for line in f:
            stones = line.split()
            break
    return sum(evolve(stone, 75) for stone in stones)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
