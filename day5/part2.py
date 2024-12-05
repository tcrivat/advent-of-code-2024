from collections import defaultdict

INPUT_FILE = "input.txt"

def solution(filename):
    successors = defaultdict(list)
    
    def solve(line):
        pages = list(map(int, line.split(",")))
        relevant = set(pages)
        remaining = set(pages)
        incorrect = False
        for page in pages:
            remaining.remove(page)
            out_of_order = {succ for succ in successors[page]
                if succ in relevant and succ not in remaining}
            if out_of_order:
                pos = min(i for i, p in enumerate(pages)
                    if p in out_of_order)
                pages.remove(page)
                pages.insert(pos, page)
                incorrect = True
        return pages[len(pages) // 2] if incorrect else 0
    
    with open(filename) as f:
        for line in f:
            if not line.strip():
                break
            p1, p2 = map(int, line.split("|"))
            successors[p1].append(p2) 
        return sum(solve(line) for line in f)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
