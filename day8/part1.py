INPUT_FILE = "input.txt"

def solution(filename):
    def on_map(i, j):
        return 0 <= i < n and 0 <= j < m
    
    with open(filename) as f:
        matrix = [line.strip() for line in f]
    n = len(matrix)
    m = len(matrix[0])
    
    antinodes = set()
    for i1 in range(n):
        for j1 in range(m):
            for i2 in range(n):
                for j2 in range(m):
                    if ((i1 != i2 or j1 != j2) and
                            matrix[i1][j1] == matrix[i2][j2] and
                            matrix[i1][j1] != "."):
                        di = i1 - i2
                        dj = j1 - j2
                        if on_map(*(a := (i1 + di, j1 + dj))):
                            antinodes.add(a)
    
    return len(antinodes)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
