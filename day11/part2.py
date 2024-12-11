INPUT_FILE = "input.txt"

memo = {}

def evolve(stone, generation):
    if generation == 0:
        return 1
    if (stone, generation) in memo:
        return memo[(stone, generation)]
    answer = 0
    if stone == "0":
        answer += evolve("1", generation - 1)
    elif len(stone) % 2 == 0:
        answer += evolve(stone[0 : len(stone) // 2], generation - 1)
        answer += evolve(str(int(stone[len(stone) // 2 :])), generation - 1)
    else:
        answer += evolve(str(int(stone) * 2024), generation - 1)
    memo[(stone, generation)] = answer
    return answer

def solution(filename):
    with open(filename) as f:
        stones = f.readline().split()
    return sum(evolve(stone, 75) for stone in stones)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
