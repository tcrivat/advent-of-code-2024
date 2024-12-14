INPUT_FILE = "input.txt"
N = 101
M = 103
SECONDS = 100

def parse_line(line):
    p, v = line.split()
    p = list(map(int, p.split("=")[1].split(",")))
    v = list(map(int, v.split("=")[1].split(",")))
    return p, v

def solution(filename):
    robots = []
    with open(filename) as f:
        for line in f:
            robots.append(parse_line(line))
    
    q = [[0] * 2, [0] * 2]
    for p, v in robots:
        p[0] = (p[0] + SECONDS * v[0]) % N
        p[1] = (p[1] + SECONDS * v[1]) % M
        if p[0] != N // 2 and p[1] != M // 2:
            q[p[0] < N // 2][p[1] < M // 2] += 1
    return q[0][0] * q[1][0] * q[0][1] * q[1][1]

if __name__ == "__main__":
    print(solution(INPUT_FILE))
