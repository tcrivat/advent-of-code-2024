"""
    I use the same Dijkstra's algorithm as in part 1 and afterwards
I reconstruct all the shortest paths backwards from the END tile
back to the START tile. I use a recursive backtracking function that
starts from the END tile and only expands the shortest paths, until
finally reaching the START tile. If the START tile was reached on a
certain path, all the tiles encountered in that path are added to a
set. The final answer is the number of elements in the set.
"""
from heapq import heapify, heappop, heappush

INPUT_FILE = "input.txt"
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def solution(filename):
    def read_input():
        with open(filename) as f:
            while line := f.readline().strip():
                matrix.append(list(line))
    
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
        neighbors = []
        next = (coord[0] + sign * dir[0], coord[1] + sign * dir[1])
        neighbors.append((dist + sign * 1, next, dir))
        for new_dir in turn(dir):
            neighbors.append((dist + sign * 1000, coord, new_dir))
        return neighbors
    
    def solve_dijkstra(start, start_dir):
        distances[(start, start_dir)] = 0
        priority_queue = [(0, start, start_dir)]
        heapify(priority_queue)
        
        while priority_queue:
            node = heappop(priority_queue)
            for dist, coord, dir in get_neighbors(node):
                if (0 <= coord[0] < n and # on map
                        0 <= coord[1] < m and
                        matrix[coord[0]][coord[1]] != "#" and # not wall
                        ((coord, dir) not in distances or # better distance
                         dist < distances[(coord, dir)])): 
                    distances[(coord, dir)] = dist
                    heappush(priority_queue, (dist, coord, dir))
    
    def search_best_paths(node):
        dist, coord, dir = node
        
        if ((coord, dir) not in distances or # not reachable
                 dist != distances[(coord, dir)]): # not on the shortest path
            return False
        
        if coord == start:
            all_best_paths.add(coord)
            return True
        
        neighbors = get_neighbors(node, backwards=True)
        reaches_start = any([search_best_paths(neighbor)
                             for neighbor in neighbors])
        if reaches_start:
            all_best_paths.add(coord)
        return reaches_start
    
    matrix = []
    read_input()
    n = len(matrix)
    m = len(matrix[0])
    start = find_position("S")
    end = find_position("E")
    
    distances = {}
    solve_dijkstra(start, (0, 1)) # EAST
    best_score = min(distances[(end, dir)]
               for dir in DIRECTIONS)
    
    all_best_paths = set()
    for dir in DIRECTIONS:
        search_best_paths((best_score, end, dir))
    return len(all_best_paths)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
