INPUT_FILE = "input.txt"

def evolve(stone):
    stones = [stone]
    for _ in range(25):
        new_stones = []
        for stone in stones:
            if stone == "0":
                new_stones.append("1")
            elif len(stone) % 2 == 0:
                new_stones.append(stone[0 : len(stone) // 2])
                new_stones.append(str(int(stone[len(stone) // 2 :])))
            else:
                new_stones.append(str(int(stone) * 2024))
        stones = new_stones
    return len(stones)

def solution(filename):
    with open(filename) as f:
        for line in f:
            stones = line.split()
            break
    return sum(evolve(stone) for stone in stones)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
