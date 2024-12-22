"""
    When moving from a key to another key, you can use at most two types of moves:
up(^)/down(v) and left(<)/right(>). For example from key 3 to key 7, you need to
use <<^^A or ^^<<A (<^<^A is surely inefficient).
    This is the correct order: left(<), up(^), down(v), right(>) - the same order
in which keys are present on the keypad! For example: left(<) always comes before
up(^) or right(>).
    You should NOT hover on top of the missing key of the keyboard! This constraint
changes the order above for some edge cases:
    For keypad 1:
    - from the last line to the first column, you put ^ before <
    - from the first column to the last line, you put > before v
    For keypad 2:
    - from the first line to the first column, you put v before <
    - from the first column to the first line, you put > before ^
"""
INPUT_FILE = "input.txt"

KEYPAD1 = {"7": (0, 0), "8": (0, 1), "9": (0, 2),
           "4": (1, 0), "5": (1, 1), "6": (1, 2),
           "1": (2, 0), "2": (2, 1), "3": (2, 2),
                        "0": (3, 1), "A": (3, 2)}

KEYPAD2 = {             "^": (0, 1), "A": (0, 2),
           "<": (1, 0), "v": (1, 1), ">": (1, 2)}

START_KEY = "A"

def solution(filename):
    def move(key1, key2, keypad):
        pos1 = keypad[key1]
        pos2 = keypad[key2]
        order = "<^v>"
        
        # exceptions that avoid hovering over the missing key
        if (keypad == KEYPAD1 and
                (pos1[0] == 3 and pos2[1] == 0 or # last line to the first column
                 pos1[1] == 0 and pos2[0] == 3)   # first column to the last line
            or keypad == KEYPAD2 and
                (pos1[0] == 0 and pos2[1] == 0 or # first line to the first column
                 pos1[1] == 0 and pos2[0] == 0)): # first column to the first line
            order = reversed(order)
        
        count = {"<": max(0, pos1[1] - pos2[1]),
                 "^": max(0, pos1[0] - pos2[0]),
                 "v": max(0, pos2[0] - pos1[0]),
                 ">": max(0, pos2[1] - pos1[1])}
        moves = [move * count[move] for move in order]
        moves.append("A")
        return "".join(moves)
    
    def process(sequence, keypad):
        moves = []
        prev = START_KEY
        for key in sequence:
            moves.append(move(prev, key, keypad))
            prev = key
        return "".join(moves)
    
    def solve(sequence):
        sequence1 = process(sequence, KEYPAD1)
        sequence2 = process(sequence1, KEYPAD2)
        sequence3 = process(sequence2, KEYPAD2)
        return len(sequence3) * int(sequence[:-1])
    
    with open(filename) as f:
        return sum(solve(line.strip()) for line in f)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
