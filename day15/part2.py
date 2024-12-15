INPUT_FILE = "input.txt"

def solution(filename):
    def find_start():
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "@":
                    return i, j
    
    def update(line):
        updated = []
        for c in line:
            match c:
                case "#":
                    updated.append("#")
                    updated.append("#")
                case "O":
                    updated.append("[")
                    updated.append("]")
                case ".":
                    updated.append(".")
                    updated.append(".")
                case "@":
                    updated.append("@")
                    updated.append(".")
        return updated
    
    def convert(move):
        match move:
            case "^":
                return -1, 0
            case "<":
                return 0, -1
            case ">":
                return 0, 1
            case "v":
                return 1, 0

    def can_push(x, y, dx, dy):
        if matrix[x + dx][y + dy] == "#":
            return False
        elif matrix[x + dx][y + dy] == ".":
            return True
        elif dx: # UP or DOWN
            if matrix[x + dx][y + dy] == "[":
                return (can_push(x + dx, y, dx, dy) and
                        can_push(x + dx, y + 1, dx, dy))
            elif matrix[x + dx][y + dy] == "]":
                return (can_push(x + dx, y - 1, dx, dy) and
                        can_push(x + dx, y, dx, dy))
        else: # LEFT or RIGHT
            return can_push(x, y + dy, dx, dy)
    
    def push(x, y, dx, dy):
        if matrix[x + dx][y + dy] == "[":
            push(x + dx, y + dy, dx, dy)
            if dx: # UP or DOWN
                push(x + dx, y + 1, dx, dy)
        elif matrix[x + dx][y + dy] == "]":
            push(x + dx, y + dy, dx, dy)
            if dx: # UP or DOWN
                push(x + dx, y - 1, dx, dy)
        matrix[x + dx][y + dy] = matrix[x][y]
        matrix[x][y] = "."

    def move_robot(x, y, dx, dy):
        if can_push(x, y, dx, dy):
            push(x, y, dx, dy)
            x += dx
            y += dy
        return x, y
    
    def sum_coordinates():
        answer = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "[":
                    answer += 100 * i + j
        return answer

    def print_map():
        for i in range(n):
            for j in range(m):
                print(matrix[i][j], end="")
            print()
    
    matrix = []
    moves = []
    with open(filename) as f:
        while line := f.readline().strip():
            matrix.append(update(line))
        while line := f.readline().strip():
            moves.append(line)
        moves = "".join(moves)
    n = len(matrix)
    m = len(matrix[0])
    x, y = find_start()
    for move in moves:
        x, y = move_robot(x, y, *convert(move))
    # print_map()
    return sum_coordinates()

if __name__ == "__main__":
    print(solution(INPUT_FILE))
