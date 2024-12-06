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
    
    def walk(i, j, di, dj, visited, check_o):
        while True:
            if not on_map(i, j):
                return False # out of the map
            if (i, j, di, dj) in visited:
                return True # walk in circles
            
            visited.add((i, j, di, dj))
            next_i = i + di
            next_j = j + dj
            
            # test if we can place an obstacle in (next_i, next_j)
            if (check_o and on_map(next_i, next_j) and
                    matrix[next_i][next_j] == "." and
                    (next_i, next_j, -1, 0) not in visited and
                    (next_i, next_j, 0, 1) not in visited and
                    (next_i, next_j, 1, 0) not in visited and
                    (next_i, next_j, 0, -1) not in visited):
                matrix[next_i][next_j] = "#"
                di_r, dj_r = turn_right(di, dj)
                circle = walk(i, j, di_r, dj_r, visited.copy(), False)
                matrix[next_i][next_j] = "."
                
                if circle:
                    nonlocal obstructions
                    obstructions += 1
            
            # if (next_i, next_j) is a wall, turn
            if on_map(next_i, next_j) and matrix[next_i][next_j] == "#":
                di, dj = turn_right(di, dj)
            else: # else advance
                i = next_i
                j = next_j
    
    with open(filename) as f:
        matrix = [list(line.strip()) for line in f]
    n = len(matrix)
    m = len(matrix[0])
    obstructions = 0
    start_i, start_j = find_start()
    visited = set()
    walk(start_i, start_j, -1, 0, visited, True) # walk up from start
    return obstructions

if __name__ == "__main__":
    print(solution(INPUT_FILE))
