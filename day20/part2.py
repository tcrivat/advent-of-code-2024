"""
    I use the same approach as in part 1, however, this time,
to find a cheat from a certain node on the track, I look at all
the other nodes that are on the track at a distance of equals or
less than 20 positions from the node.
    To iterate through these positions, I wrote a function that
returns a list with all the positions (neighbors) at a certain
distance from a node. This is implemented using a simple iterative
algorithm.
"""
INPUT_FILE = "input.txt"
MAX_DISTANCE = 20
MIN_CHEAT_TIME = 100

def solution(filename):
    def read_input():
        matrix = []
        with open(filename) as f:
            while line := f.readline().strip():
                matrix.append(list(line))
        return matrix
    
    def find_node(symbol):
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == symbol:
                    return i, j
    
    def get_all_neighbors(node, dist):
        delta_i, delta_j = -dist, 0
        dir_i, dir_j = -1, 1
        first = None
        while (delta_i, delta_j) != first:
            if not first:
                first = (delta_i, delta_j)
            yield (node[0] + delta_i, node[1] + delta_j)
            if abs(delta_i) == dist:
                dir_i *= -1
            if abs(delta_j) == dist:
                dir_j *= -1
            delta_i += dir_i
            delta_j += dir_j
    
    def get_neighbors(node, dist, symbol):
        for neigh in get_all_neighbors(node, dist):
            if (0 <= neigh[0] < n and # on map
                    0 <= neigh[1] < m and
                    matrix[neigh[0]][neigh[1]] == symbol):
                yield neigh
    
    def get_racetrack(start, end):
        track = [start]
        score = {start: 0}
        node = start
        while node != end:
            for next in get_neighbors(node, 1, "."):
                if next not in score:
                    score[next] = score[node] + 1
                    track.append(next)
                    node = next
                    break
        return track, score
    
    def try_cheating(node):
        cheats = 0
        for dist in range(2, MAX_DISTANCE + 1):
            for neigh in get_neighbors(node, dist, "."):
                cheat_time = score[neigh] - score[node] - dist
                if cheat_time >= MIN_CHEAT_TIME:
                    cheats += 1
        return cheats
    
    matrix = read_input()
    n = len(matrix)
    m = len(matrix[0])
    start = find_node("S")
    end = find_node("E")
    matrix[start[0]][start[1]] = "."
    matrix[end[0]][end[1]] = "."
    
    racetrack, score = get_racetrack(start, end)
    return sum(try_cheating(node) for node in racetrack)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
