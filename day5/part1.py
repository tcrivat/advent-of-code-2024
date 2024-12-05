from collections import defaultdict

INPUT_FILE = "input.txt"

def solution(filename):
    successors = defaultdict(set)
    
    def solve(line):
        pages = list(map(int, line.split(",")))
        relevant = set(pages)
        remaining = set(pages)
        for page in pages:
            remaining.remove(page)
            for succ in successors[page]:
                if succ in relevant and succ not in remaining:
                    return 0
        return pages[len(pages) // 2]
    
    with open(filename) as f:
        for line in f:
            if not line.strip():
                break
            n1, n2 = map(int, line.split("|"))
            successors[n1].add(n2) 
        return sum(solve(line) for line in f)
    
if __name__ == "__main__":
    print(solution(INPUT_FILE))
