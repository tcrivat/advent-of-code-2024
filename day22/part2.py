from collections import deque, defaultdict

INPUT_FILE = "input.txt"
ITERATIONS = 2000
LAST_24_BITS = (1 << 24) - 1

def solution(filename):
    def process_input(secret):
        visited = set()
        last4 = deque(maxlen=4)
        prev_price = secret % 10
        
        for i in range(ITERATIONS):
            secret ^= (secret << 6) & LAST_24_BITS
            secret ^= (secret >> 5) & LAST_24_BITS
            secret ^= (secret << 11) & LAST_24_BITS
            
            price = secret % 10
            change = price - prev_price
            prev_price = price
            last4.append(change)
            
            if len(last4) < 4:
                continue
            
            seq = tuple(last4)
            if seq not in visited:
                visited.add(seq)
                bananas[seq] += price
    
    bananas = defaultdict(int)
    with open(filename) as f:
        for line in f:
            process_input(int(line.strip()))
    return max(bananas.values())

if __name__ == "__main__":
    print(solution(INPUT_FILE))
