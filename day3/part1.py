import re

INPUT_FILE = "input.txt"

def solution(filename):
    with open(filename) as f:
        program = f.read().replace("\n", "")
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", program)
    return sum(int(n1) * int(n2) for n1, n2 in matches)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
