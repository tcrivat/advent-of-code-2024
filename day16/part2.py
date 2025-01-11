"""
    I use the same Dijkstra's algorithm as in part 1 and afterwards
I reconstruct all the shortest paths backwards from the END tile
back to the START tile. I use DFS to enumerate all the nodes on the
shortest path, for each node choosing only the neighbor (predecessor)
that is on the shortest path (its shortest distance from START should
be equal with the current's node shortest distance minus the distance
between the nodes). I keep all the encountered nodes in a set. The
final answer is the number of elements in the set.
"""
from heapq import heapify, heappop, heappush

INPUT_FILE = "input.txt"
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def solution(filename):
    def read_input():
        matrix = []
        with open(filename) as f:
            while line := f.readline().strip():
                matrix.append(line)
        return matrix
    
    def find_position(symbol):
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == symbol:
                    return i, j
    
    def turn(dir):
        if dir[0]:
            return [(0, -1), (0, 1)]
        else:
            return [(-1, 0), (1, 0)]
    
    def get_neighbors(node, backwards=False):
        dist, coord, dir = node
        sign = -1 if backwards else 1
        next = (coord[0] + sign * dir[0], coord[1] + sign * dir[1])
        if (0 <= next[0] < n and # on map
                0 <= next[1] < m and
                matrix[next[0]][next[1]] != "#"): # not wall
            yield (dist + sign * 1, next, dir)
        for new_dir in turn(dir):
            yield (dist + sign * 1000, coord, new_dir)
    
    def solve_dijkstra(start, start_dir):
        best_score = None
        distances[(start, start_dir)] = 0
        priority_queue = [(0, start, start_dir)]
        heapify(priority_queue)
        
        while priority_queue:
            node = heappop(priority_queue)
            for dist, coord, dir in get_neighbors(node):
                if (dist < distances.get((coord, dir), dist + 1)): 
                    if coord == end and not best_score:
                        best_score = dist
                    distances[(coord, dir)] = dist
                    heappush(priority_queue, (dist, coord, dir))
        return best_score
    
    def search_dfs(node):
        dist, coord, dir = node
        if ((coord, dir) not in distances or # not reachable
                 dist != distances[(coord, dir)]): # not on the shortest path
            return
        all_best_paths.add(coord)
        for neighbor in get_neighbors(node, backwards=True):
            search_dfs(neighbor)
    
    matrix = read_input()
    n = len(matrix)
    m = len(matrix[0])
    start = find_position("S")
    end = find_position("E")
    
    distances = {}
    best_score = solve_dijkstra(start, (0, 1)) # EAST
    
    all_best_paths = set()
    for dir in DIRECTIONS:
        search_dfs((best_score, end, dir))
    return len(all_best_paths)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
