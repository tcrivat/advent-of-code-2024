"""
    Same implementation as for part 1, just that now I
add the blocked positions one by one and test each time
if there is still a path between START and END with BFS.
"""
from collections import deque

INPUT_FILE = "input.txt"
N = 71
POSITIONS = 1024
START = (0, 0)
END = (N - 1, N - 1)
DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solution(filename):
    def read_positions():
        with open(filename) as f:
            while line := f.readline().strip():
                x, y = map(int, line.split(","))
                yield (x, y)
    
    def solve_bfs():
        dist = {START: 0}
        queue = deque([START])
        while queue:
            node = queue.popleft()
            for d in DIR:
                next = (node[0] + d[0], node[1] + d[1])
                if (0 <= next[0] < N and # on map
                        0 <= next[1] < N and
                        next not in blocked and # not wall
                        next not in dist): # not visited
                    dist[next] = dist[node] + 1
                    if next == END:
                        return dist[END]
                    else:
                        queue.append(next)
        return -1
    
    input = read_positions()
    blocked = set(next(input) for _ in range(POSITIONS))
    for pos in input:
        blocked.add(pos)
        if solve_bfs() == -1: # not reachable
            return f"{pos[0]},{pos[1]}"

if __name__ == "__main__":
    print(solution(INPUT_FILE))
