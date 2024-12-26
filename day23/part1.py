"""
    I start with all the nodes that start with the letter
"t", iterate through all the adjacent nodes and for each
node, iterate through all of their adjacent nodes that are
connected to the first node. To ensure the uniqueness, I
sort these tree nodes by name, convert to a tuple and add
it to a set. The puzzle's answer represents the length of
this set.
"""
from collections import defaultdict

INPUT_FILE = "input.txt"

def solution(filename):
    adj = defaultdict(set)
    with open(filename) as f:
        for line in f:
            node1, node2 = line.strip().split("-")
            adj[node1].add(node2)
            adj[node2].add(node1)
    
    sets_of_3 = set()
    for node1 in adj:
        if node1[0] == "t":
            for node2 in adj[node1]:
                for node3 in adj[node2]:
                    if node1 in adj[node3]:
                        s = [node1, node2, node3]
                        sets_of_3.add(tuple(sorted(s)))
    return len(sets_of_3)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
