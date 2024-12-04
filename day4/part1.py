INPUT_FILE = "input.txt"
WORD = "XMAS"

def solution(filename):
    matrix = []
    with open(filename) as f:
        for line in f:
            matrix.append(line.strip())
    n = len(matrix)
    m = len(matrix[0])

    def match(i, j, p, di, dj):
        if (i < 0 or j < 0 or i == n or j == m
                or matrix[i][j] != WORD[p]):
            return 0
        if p == len(WORD) - 1:
            return 1
        return match(i + di, j + dj, p + 1, di, dj)
    
    def search(i, j):
        return sum(match(i, j, 0, di, dj)
            for di in [-1, 0, 1]
            for dj in [-1, 0, 1]
            if di or dj)

    return sum(search(i, j) for i in range(n)
                            for j in range(m))

if __name__ == "__main__":
    print(solution(INPUT_FILE))
