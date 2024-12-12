INPUT_FILE = "input.txt"

def solution(filename):
    def visit(i, j, value, region):
        if not (0 <= i < n and 0 <= j < m and
                matrix[i][j] == value and visited[i][j] == -1):
            return
        visited[i][j] = region
        for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            visit(i + di, j + dj, value, region)
    
    def identify_regions():
        regions = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j] == -1:
                    visit(i, j, matrix[i][j], regions)
                    regions += 1
        return regions
    
    def count():
        area = [0] * r
        perimeter = [0] * r
        for i in range(n):
            for j in range(m):
                region = visited[i][j]
                area[region] += 1
                for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    if (not (0 <= i + di < n and 0 <= j + dj < m)
                            or matrix[i + di][j + dj] != matrix[i][j]):
                        # edge of the map or neighbor of different type
                        perimeter[region] += 1
        return area, perimeter
    
    with open(filename) as f:
        matrix = [line.strip() for line in f]
    n = len(matrix)
    m = len(matrix[0])
    visited = [[-1] * m for _ in range(n)] # -1 = not visited yet
    r = identify_regions()
    return sum(area * perimeter for area, perimeter in zip(*count()))

if __name__ == "__main__":
    print(solution(INPUT_FILE))
