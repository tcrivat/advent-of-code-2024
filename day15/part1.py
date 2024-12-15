INPUT_FILE = "input.txt"

def solution(filename):
    def read_input(filename):
        with open(filename) as f:
            while line := f.readline().strip():
                matrix.append(list(line))
            while line := f.readline().strip():
                convert = {"^" : (-1, 0), "<" : (0, -1),
                           ">" : ( 0, 1), "v" : (1,  0)}
                moves.extend(map(lambda x: convert[x], line))
    
    def find_start():
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "@":
                    return i, j
    
    def move_robot(x, y, dx, dy):
        next_x, next_y = x + dx, y + dy
        while matrix[next_x][next_y] == "O":
            next_x += dx
            next_y += dy
        if matrix[next_x][next_y] == ".":
            matrix[next_x][next_y] = matrix[next_x - dx][next_y - dy]
            matrix[x][y] = "."
            x += dx
            y += dy
            matrix[x][y] = "@"
        return x, y
    
    def sum_coordinates():
        answer = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "O":
                    answer += 100 * i + j
        return answer
    
    matrix = []
    moves = []
    read_input(filename)
    n = len(matrix)
    m = len(matrix[0])
    x, y = find_start()
    for direction in moves:
        x, y = move_robot(x, y, *direction)
    return sum_coordinates()

if __name__ == "__main__":
    print(solution(INPUT_FILE))
