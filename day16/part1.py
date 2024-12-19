"""
    The solution uses Dijkstra's algorithm to compute the shortest
path between the START and END tiles. To take into account changing
direction (turning left or right 90 degrees) and its associated
cost, each tile from the map is associated with 4 nodes, one for
each direction from which the tile could be reached.
    So a node is a tuple which contains the coordinates of the tile
and a direction. A node has 3 neighbors:
    - the tile in front, same direction, cost 1
    - the same tile, direction 90 deg. to the right, cost 1000
    - the same tile, direction 90 deg. to the left, cost 1000
    After running the algorithm, we have 4 node associated with the
end tile, each with possibly different scores. We return the
minimum of these scores.
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
    
    def get_neighbors(node):
        dist, coord, dir = node
        neighbors = []
        next = (coord[0] + dir[0], coord[1] + dir[1])
        neighbors.append((dist + 1, next, dir))
        for new_dir in turn(dir):
            neighbors.append((dist + 1000, coord, new_dir))
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
    
    matrix = []
    read_input()
    n = len(matrix)
    m = len(matrix[0])
    start = find_position("S")
    end = find_position("E")
    
    distances = {}
    solve_dijkstra(start, (0, 1)) # EAST
    return min(distances[(end, dir)]
               for dir in DIRECTIONS)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
