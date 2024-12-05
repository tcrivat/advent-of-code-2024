from collections import defaultdict

INPUT_FILE = "input.txt"

def solution(filename):
    succ = defaultdict(set)
    
    def solve(line):
        pages = list(map(int, line.split(",")))
        relevant = set(pages)
        remaining = set(pages)
        for page in pages:
            remaining.remove(page)
            relevant_succ = succ[page].intersection(relevant)
            if not relevant_succ.issubset(remaining):
                return 0
        return pages[len(pages) // 2]
    
    with open(filename) as f:
        for line in f:
            if not line.strip():
                break
            n1, n2 = map(int, line.split("|"))
            succ[n1].add(n2) 
        return sum(solve(line) for line in f)
    
if __name__ == "__main__":
    print(solution(INPUT_FILE))
