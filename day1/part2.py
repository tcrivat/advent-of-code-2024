INPUT_FILE = "input.txt"

def solution(filename):
    d1, d2 = {}, {}
    with open(filename) as f:
        for line in f:
            n1, n2 = map(int, line.split())
            d1[n1] = d1.get(n1, 0) + 1
            d2[n2] = d2.get(n2, 0) + 1
    answer = 0
    for n in d1:
        answer += n * d1[n] * d2.get(n, 0)
    return answer

if __name__ == "__main__":
    print(solution(INPUT_FILE))
