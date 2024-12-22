INPUT_FILE = "input.txt"
ITERATIONS = 2000

def solution(filename):
    def shift(x, n):
        if n > 0:
            return (x << n) & ((1 << 24) - 1)
        else:
            return x >> -n
    
    def solve(initial_secret):
        secret = initial_secret
        for _ in range(ITERATIONS):
            secret ^= shift(secret, 6)
            secret ^= shift(secret, -5)
            secret ^= shift(secret, 11)
        return secret
    
    with open(filename) as f:
        return sum(solve(int(line.strip())) for line in f)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
