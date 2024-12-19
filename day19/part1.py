"""
    Dynammic programming solution (bottom-up) that tests if
a substring containing the first i characters from the string
can be formed by combining the given patterns.
    The base case: an empty string is always valid.
        dp[0] = True
    To compute dp[i], we test if any of the patterns could be
matched at the end of the current string (first i characters). If
this is the case and the current string minus the pattern is also
valid, we conclude that the current string is valid.
        dp[i] = True if substring ends in pattern
                        and dp[i - len(pattern)] is also True
    The whole string is valid if dp[n] (with n = the length of the
string) is valid.
    I also did another optimization that uses the hash codes of the
patterns instead of the patterns themselves. A string is considered
to end with a pattern if the hash code of a set of characters in its
tail matches the hash code of a pattern. This relies on the fact
that hash code collisions are very rare (which is the case).
"""
INPUT_FILE = "input.txt"

def solution(filename):
    def is_possible(design):
        n = len(design)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for m in range(1, min(i, max_length) + 1):
                h = hash(design[i - m : i])
                if (h in hashes and dp[i - m]):
                    dp[i] = True
                    break
        return dp[n]
    
    with open(filename) as f:
        patterns = f.readline().strip().split(", ")
        max_length = max(len(p) for p in patterns)
        hashes = set(hash(p) for p in patterns)
        f.readline()
        return sum(is_possible(line.strip()) for line in f)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
