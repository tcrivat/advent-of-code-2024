from collections import defaultdict

INPUT_FILE = "input.txt"

def solution(filename):
    succ = defaultdict(set)
    
    def solve(line):
        pages = list(map(int, line.split(",")))
        relevant = set(pages)
        remaining = set(pages)
        incorrect = False
        for page in pages:
            remaining.remove(page)
            relevant_succ = succ[page].intersection(relevant)
            out_of_order = relevant_succ.difference(remaining)
            if out_of_order:
                pos = min(pages.index(p) for p in out_of_order)
                pages.remove(page)
                pages.insert(pos, page)
                incorrect = True
        return pages[len(pages) // 2] if incorrect else 0
    
    with open(filename) as f:
        for line in f:
            if not line.strip():
                break
            n1, n2 = map(int, line.split("|"))
            succ[n1].add(n2) 
        return sum(solve(line) for line in f)
    
if __name__ == "__main__":
    print(solution(INPUT_FILE))
