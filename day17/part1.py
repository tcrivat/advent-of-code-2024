"""
    Simple implementation, I just parse the program and
execute the instructions.
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
    
    with open(filename) as f:
        A = int(parse(f.readline()))
        B = int(parse(f.readline()))
        C = int(parse(f.readline()))
        f.readline()
        program = list(map(int, parse(f.readline()).split(",")))
    
    output = run_program(A, B, C, program)
    return ",".join(map(str, output))

if __name__ == "__main__":
    print(solution(INPUT_FILE))
