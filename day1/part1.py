INPUT_FILE = "input.txt"

def solution(filename):
    l1, l2 = [], []
    with open(filename) as f:
        for line in f:
            n1, n2 = map(int, line.split())
            l1.append(n1)
            l2.append(n2)
    l1.sort()
    l2.sort()
    answer = 0
    for n1, n2 in zip(l1, l2):
        answer += abs(n1 - n2)
    return answer

if __name__ == "__main__":
    print(solution(INPUT_FILE))
