INPUT_FILE = "input.txt"
SIZE = 5

def solution(filename):
    def fit(key, lock):
        for p1, p2 in zip(lock, key):
            if p1 + p2 > SIZE:
                return False
        return True
    
    def read_input():
        keys = set()
        locks = set()
        with open(filename) as f:
            while first := f.readline().strip():
                lock = first == "#" * SIZE
                heights = [0] * SIZE
                for _ in range(SIZE):
                    line = f.readline().strip()
                    for i, c in enumerate(line):
                        heights[i] += c == "#"
                f.readline()
                f.readline()
                heights = tuple(heights)
                if lock:
                    locks.add(heights)
                else:
                    keys.add(heights)
        return keys, locks
    
    keys, locks = read_input()
    return sum(fit(key, lock) for key in keys for lock in locks)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
