from collections import defaultdict

INPUT_FILE = "input.txt"

def solution(filename):
    f1, f2 = defaultdict(int), defaultdict(int)
    with open(filename) as f:
        for line in f:
            n1, n2 = map(int, line.split())
            f1[n1] += 1
            f2[n2] += 1
    return sum(n * f1[n] * f2[n] for n in f1)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
