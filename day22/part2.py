from collections import deque, defaultdict

INPUT_FILE = "input.txt"
ITERATIONS = 2000

def solution(filename):
    def shift(x, n):
        if n > 0:
            return (x << n) & ((1 << 24) - 1)
        else:
            return x >> -n
    
    def process_input(secret):
        last4 = deque()
        visited = set()
        for i in range(ITERATIONS):
            prev_price = secret % 10
            
            secret ^= shift(secret, 6)
            secret ^= shift(secret, -5)
            secret ^= shift(secret, 11)
            
            price = secret % 10
            change = price - prev_price
            last4.append(change)
            
            if i < 3:
                continue
            elif i > 3:
                last4.popleft()
            
            if (seq := tuple(last4)) in visited:
                continue
            visited.add(seq)
            bananas[seq] += price
    
    bananas = defaultdict(int)
    with open(filename) as f:
        for line in f:
            process_input(int(line.strip()))
    return max(bananas.values())

if __name__ == "__main__":
    print(solution(INPUT_FILE))
