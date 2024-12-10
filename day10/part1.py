INPUT_FILE = "input.txt"

def solution(filename):
    def trailheads(i, j, altitude):
        if not (0 <= i < n and 0 <= j < m and matrix[i][j] == altitude):
            return set()
        if altitude == 9:
            return set([(i, j)])
        return set().union(*[trailheads(i + di, j + dj, altitude + 1)
                   for di in [-1, 0, 1]
                   for dj in [-1, 0, 1]
                   if di and not dj or not di and dj])
    
    with open(filename) as f:
        matrix = [list(map(int, line.strip())) for line in f]
    n = len(matrix)
    m = len(matrix[0])
    return sum(len(trailheads(i, j, 0))
               for i in range(n)
               for j in range(m))

if __name__ == "__main__":
    print(solution(INPUT_FILE))

