from collections import defaultdict

INPUT_FILE = "input.txt"

def solution(filename):
    f1, f2 = defaultdict(int), defaultdict(int)
    with open(filename) as f:
        for line in f:
            n1, n2 = map(int, line.split())
            f1[n1] += 1
            f2[n2] += 1
    answer = 0
    for n in f1:
        answer += n * f1[n] * f2[n]
    return answer

if __name__ == "__main__":
    print(solution(INPUT_FILE))
