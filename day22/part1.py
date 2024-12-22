"""
    An alternative way of transforming the number:
- shift 6 bits to the left, keep the last 24 bits and XOR with the previous value
- shift 5 bits to the right and XOR with the previous value
- shift 11 bits to the left, keep the last 24 bits and XOR with the previous value
"""
INPUT_FILE = "input.txt"
ITERATIONS = 2000
LAST_24_BITS = (1 << 24) - 1

def solution(filename):
    def solve(secret):
        for _ in range(ITERATIONS):
            secret ^= (secret << 6) & LAST_24_BITS
            secret ^= (secret >> 5) & LAST_24_BITS
            secret ^= (secret << 11) & LAST_24_BITS
        return secret
    
    with open(filename) as f:
        return sum(solve(int(line.strip())) for line in f)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
