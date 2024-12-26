"""
    The problem can be rephrased as finding the maximum clique in an
undirected graph. I used a version of the Bron-Kerbosch algorithm,
simplified so that only the largest clique is returned.
    This is implemented using a recursive backtracking algorithm that
receives two parameters:
    * clique: a set of nodes added so far to the clique
    * candidates: a set of potential candidates to be added to the clique
    Note that only nodes that are connected to all the other nodes in
the clique are considered as candidates. The algorithm iterates through
the set of candidates and tries to either add it to the clique (using a
recursive call) or removes it from the list of candidates and then tries
the next candidate (after returning from the recursive call).
"""
from collections import defaultdict

INPUT_FILE = "input.txt"

def solution(filename):
    def search(clique, candidates):
        max_clique = clique
        while candidates:
            node = candidates.pop()
            new_clique = search(clique | {node}, candidates & adj[node])
            max_clique = max(max_clique, new_clique, key=len)
        return max_clique
    
    adj = defaultdict(set)
    with open(filename) as f:
        for line in f:
            node1, node2 = line.strip().split("-")
            adj[node1].add(node2)
            adj[node2].add(node1)
    return ",".join(sorted(search(set(), set(adj))))

if __name__ == "__main__":
    print(solution(INPUT_FILE))
