INPUT_FILE = "input.txt"

def solution(filename):
    def find_start():
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "^":
                    return i, j
    
    def turn_right(di, dj):
        if di == -1 and dj == 0: # up -> right
            return 0, 1
        elif di == 0 and dj == 1: # right -> down
            return 1, 0
        elif di == 1 and dj == 0: # down -> left
            return 0, -1
        elif di == 0 and dj == -1: # left -> up
            return -1, 0
    
    def on_map(i, j):
        return 0 <= i < n and 0 <= j < m
    
    def walk(i, j, di, dj, visited):
        while on_map(i, j):
            visited.add((i, j))
            next_i = i + di
            next_j = j + dj
            
            # if (next_i, next_j) is a wall, turn right
            if on_map(next_i, next_j) and matrix[next_i][next_j] == "#":
                di, dj = turn_right(di, dj)
            else: # else advance in the same direction
                i = next_i
                j = next_j
    
    with open(filename) as f:
        matrix = [list(line.strip()) for line in f]
    n = len(matrix)
    m = len(matrix[0])
    start_i, start_j = find_start()
    visited = set()
    walk(start_i, start_j, -1, 0, visited) # walk up from start
    return len(visited)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
