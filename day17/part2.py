"""
    The assembly program computes a value in register B, prints it,
then divides register A by 8 and then loops again to the beginning.
The cycle stops when A becomes 0. So at each step, A is shifted 3
bits to the right (divide by 8 means shifting 3 bits to the right). 
    This means that the last value printed is computed only from the
most significant 3 bits of A, the previous before the last value is
computed from the most significant 6 bits, and so on.
    We can work backwards and determine the value of A 3 bits at a
time. We first try all the possible values for the first three bits and
choose a combination that outputs the last value correctly. To check
the program's output for a certain value of A, we run the program until
it outputs the first value. If it's not correct, we continue searching
for another value. If it's correct, we can move to the next three bits
and choose a combination that outputs the previous before the last value
correctly. And so on.
    Sometimes a certain combination of bits will lead to a dead end
(no value can match the output at a certain level), we then backtrack
and try another combination at the lower level. So the search is
implemented using a recursive backtracking algorithm.
    As there are only 8 possible value for each group of 3 bits and
at most 16 levels (groups of 3 bits), and also very few of the
combinations could lead to solutions, the algorithm (even if it has
exponential complexity 3^16), finishes very fast (tens of milliseconds).
"""
INPUT_FILE = "input.txt"

def run_program(a, b, c, program):
    def combo_to_literal(operand):
        if operand <= 3:
            return operand
        elif operand == 4:
            return a
        elif operand == 5:
            return b
        elif operand == 6:
            return c
    
    def execute(opcode, operand):
        nonlocal a, b, c, ip
        # print(f"executing {opcode=}, {operand=}")
        match opcode:
            case 0: # adv
                operand = 1 << combo_to_literal(operand)
                a //= operand
            case 1: # bxl
                b ^= operand
            case 2: # bst
                b = combo_to_literal(operand) % 8
            case 3: # jnz
                if a:
                    ip = operand - 2
            case 4: # bxc
                b ^= c
            case 5: # out
                operand = combo_to_literal(operand) % 8
                output.append(operand)
            case 6: # bdv
                operand = 1 << combo_to_literal(operand)
                b = a // operand
            case 7: # cdv
                operand = 1 << combo_to_literal(operand)
                c = a // operand
        ip += 2
    
    ip = 0 # instruction pointer
    output = []
    # print(f"{a=}, {b=}, {c=}")
    while ip < len(program):
        execute(program[ip], program[ip + 1])
        # print(f"{a=}, {b=}, {c=}")
    return output

def solution(filename):
    def parse(line):
        return line.split(": ")[1]
    
    def remove_jumps(program):
        new_program = program[:]
        for i in range(len(new_program)):
            if i % 2 == 0 and new_program[i] == 3: # jnz
                new_program[i] = -1 # no op
        return new_program
    
    def search(a, i):
        if i < 0:
            return a
        a <<= 3
        for a in range(a, a + (1 << 3)):
            out = run_program(a, B, C, program_no_jumps)[0]
            if out == program[i] and (ans := search(a, i - 1)):
                return ans
        return 0
    
    with open(filename) as f:
        A = int(parse(f.readline()))
        B = int(parse(f.readline()))
        C = int(parse(f.readline()))
        f.readline()
        program = list(map(int, parse(f.readline()).split(",")))
    
    program_no_jumps = remove_jumps(program)
    return search(0, len(program) - 1)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
