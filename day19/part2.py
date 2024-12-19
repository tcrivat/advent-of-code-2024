"""
    Same botton-up dynammic programming implementation with
the hashes optimization as for part 1, the only difference
is that in the dp array holds the number of possible combinations
instead of a boolean. I do not break the search when the first
combination is found, so I count them all.
"""
INPUT_FILE = "input.txt"

def solution(filename):
    def is_possible(design):
        n = len(design)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for m in range(1, min(i, max_length) + 1):
                if (design[i - m : i] in patterns):
                    dp[i] += dp[i - m]
        return dp[n]
    
    with open(filename) as f:
        patterns = set(f.readline().strip().split(", "))
        max_length = max(len(p) for p in patterns)
        f.readline()
        return sum(is_possible(line.strip()) for line in f)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
