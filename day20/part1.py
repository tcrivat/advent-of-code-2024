"""
    I assemble a list of every position in the racetrack and
assign a score to every such position, which represents the
number of nanoseconds to reach that position from the start.
    To assemble the list, I start with the start position and
look for neighbors that are not walls and have not been visited
yet (do not have a score assigned). As the track has only one path,
there will only be one such neighbor for every node in the track
(with the exception of the end node).
    Then for each node in the track I try to look for positions
that allow cheating. To do that, I look at every wall bordering
that node, and for every such wall, I look at its neighbors that
are on the track. The difference in scores between this node and
the initial node, minus 2, will give the number of seconds saved
by the cheat.
"""
INPUT_FILE = "input.txt"
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
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
    
    def get_neighbors(node, symbol):
        for dir in DIRECTIONS:
            neigh = node[0] + dir[0], node[1] + dir[1]
            if (0 <= neigh[0] < n and # on map
                    0 <= neigh[1] < m and
                    matrix[neigh[0]][neigh[1]] == symbol):
                yield neigh
    
    def get_racetrack(start, end):
        track = [start]
        score = {start: 0}
        node = start
        while node != end:
            for next in get_neighbors(node, "."):
                if next not in score:
                    score[next] = score[node] + 1
                    track.append(next)
                    node = next
                    break
        return track, score
    
    def try_cheating(node):
        cheats = 0
        for wall in get_neighbors(node, "#"):
            for next in get_neighbors(wall, "."):
                cheat_time = score[next] - score[node] - 2
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
