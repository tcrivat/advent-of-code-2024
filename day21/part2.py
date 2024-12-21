INPUT_FILE = "input.txt"

KEYPAD1 = {"7": (0, 0), "8": (0, 1), "9": (0, 2),
           "4": (1, 0), "5": (1, 1), "6": (1, 2),
           "1": (2, 0), "2": (2, 1), "3": (2, 2),
                        "0": (3, 1), "A": (3, 2)}

KEYPAD2 = {             "^": (0, 1), "A": (0, 2),
           "<": (1, 0), "v": (1, 1), ">": (1, 2)}

START_KEY = "A"

memo = {}

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
    
    def count(sequence, iterations):
        if (sequence, iterations) in memo:
            return memo[(sequence, iterations)]
        
        if iterations == 0:
            return len(sequence)
        
        length = 0
        prev = START_KEY
        for key in sequence:
            moves = move(prev, key, KEYPAD2)
            length += count(moves, iterations - 1)
            prev = key
        
        memo[(sequence, iterations)] = length
        return length
    
    def process(sequence, keypad):
        moves = []
        prev = START_KEY
        for key in sequence:
            moves.append(move(prev, key, keypad))
            prev = key
        return "".join(moves)
    
    def solve(sequence):
        sequence1 = process(sequence, KEYPAD1)
        length = count(sequence1, 25)
        return length * int(sequence[:-1])
    
    with open(filename) as f:
        return sum(solve(line.strip()) for line in f)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
