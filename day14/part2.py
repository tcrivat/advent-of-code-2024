INPUT_FILE = "input.txt"
N = 101
M = 103

def parse_line(line):
    p, v = line.split()
    p = list(map(int, p.split("=")[1].split(",")))
    v = list(map(int, v.split("=")[1].split(",")))
    return p, v

def print_map(matrix):
    for i in range(M):
        for j in range(N):
            if not matrix[i][j]:
                print(".", end="")
            else:
                print(matrix[i][j], end="")
        print()
    print()

def solution(filename):
    robots = []
    with open(filename) as f:
        for line in f:
            robots.append(parse_line(line))
    
    seconds = 0
    tree_found = False
    while not tree_found:
        seconds += 1
        matrix = [[0] * N for _ in range(M)]
        for p, v in robots:
            p[0] = (p[0] + v[0]) % N
            p[1] = (p[1] + v[1]) % M
            matrix[p[1]][p[0]] += 1
            neighbors = sum(bool(matrix[p[1] + dx][p[0] + dy])
                for dx in [-1, 0, 1]
                for dy in [-1, 0, 1]
                if 0 <= p[1] + dx < M and 0 <= p[0] + dy < N)
            if neighbors == 9: # full 3x3 square
                tree_found = True
    print_map(matrix)
    return seconds

if __name__ == "__main__":
    print(solution(INPUT_FILE))
