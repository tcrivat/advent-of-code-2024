INPUT_FILE = "input.txt"

def safe(levels):
    increasing = levels[0] < levels[1]
    for i in range(1, len(levels)):
        if increasing and levels[i - 1] > levels[i]:
            return 0
        if not increasing and levels[i - 1] < levels[i]:
            return 0
        if not (1 <= abs(levels[i] - levels[i - 1]) <= 3):
            return 0
    return 1

def solve(line):
    levels = list(map(int, line.split()))
    if safe(levels):
       return 1
    for i in range(len(levels)):
        new_levels = levels[:]
        del new_levels[i]
        if safe(new_levels):
           return 1
    return 0

def solution(filename):
    with open(filename) as f:
        return sum(solve(line) for line in f)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
