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
    return sum(abs(n1 - n2) for n1, n2 in zip(l1, l2))

if __name__ == "__main__":
    print(solution(INPUT_FILE))
