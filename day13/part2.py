INPUT_FILE = "input.txt"

def parse_line(line):
    line = line.replace("+", "=")
    x, y = line.split(": ")[1].split(", ")
    x = int(x.split("=")[1])
    y = int(y.split("=")[1])
    return x, y

def parse_machine(button_a, button_b, prize):
    ax, ay = parse_line(button_a)
    bx, by = parse_line(button_b)
    x, y = parse_line(prize)
    x = 10000000000000 + x
    y = 10000000000000 + y
    return ax, ay, bx, by, x, y

def solve(ax, ay, bx, by, x, y):
    n1 = by * x - bx * y
    n2 = -ay * x + ax * y
    n3 = ax * by - ay * bx
    if n1 % n3 == 0 and n2 % n3 == 0:
        a = n1 // n3
        b = n2 // n3
    else:
        a = 0
        b = 0
    return 3 * a + 1 * b

def solution(filename):
    answer = 0
    with open(filename) as f:
        while True:
            if not (button_a := f.readline()):
                break
            if not (button_b := f.readline()):
                break
            if not (prize := f.readline()):
                break
            f.readline()
            answer += solve(*parse_machine(button_a, button_b, prize))
    return answer

if __name__ == "__main__":
    print(solution(INPUT_FILE))

