INPUT_FILE = "input.txt"
ITERATIONS = 2000

def solution(filename):
    def shift(x, n):
        if n > 0:
            return (x << n) & ((1 << 24) - 1)
        else:
            return x >> -n
    
    def process_input(initial_secret):
        new_prices = []
        new_changes = []
        secret = initial_secret
        for _ in range(ITERATIONS):
            prev = secret
            secret ^= shift(secret, 6)
            secret ^= shift(secret, -5)
            secret ^= shift(secret, 11)
            new_prices.append(secret % 10)
            new_changes.append(chr(ord("a") + secret % 10 - prev % 10 + 9))
        prices.append("".join(map(str, new_prices)))
        changes.append("".join(new_changes))
    
    def get_best_sequences():
        frequencies = {}
        for i in range(n):
            for j in range(3, ITERATIONS):
                last4 = changes[i][j - 3 : j + 1]
                if last4 not in frequencies:
                    frequencies[last4] = 0
                frequencies[last4] += 1
        sequences = [(frequencies[seq], seq) for seq in frequencies]
        sequences.sort(reverse=True)
        return sequences[:50] # use only the 50 most frequent sequences
    
    def solve():
        max_bananas = 0
        for _, s in sequences:
            bananas = 0
            for i in range(n):
                if (p := changes[i].find(s)) != -1:
                    bananas += int(prices[i][p + 3])
            max_bananas = max(bananas, max_bananas)
        return max_bananas
    
    prices = []
    changes = []
    with open(filename) as f:
        for line in f:
            process_input(int(line.strip()))
    n = len(changes)
    sequences = get_best_sequences()
    return solve()

if __name__ == "__main__":
    print(solution(INPUT_FILE))
