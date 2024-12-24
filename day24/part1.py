"""
    I read the wires and gates from the input file and store
the values in two dictionaries:
    wires: the key is the wire's name, the value is the wire's value
    gates: the key is the output wire (as a wire can be connected to
at most one gate output), the value represents the input wires and the
operation performed by the gate.
    To determine the output of the gates, I start with the gates
that have the z wires connected to the output and recursively call
the function for the inputs, until I find gates that can be executed
immediately. On returning from the recursive call, I execute all the
gates on the way. This is to make sure that gates are executed in the
right order (only after all the inputs are determined).
"""
INPUT_FILE = "input.txt"
WIRE_MAX = 45

def solution(filename):
    def read_input():
        wires = {}
        gates = {}
        with open(filename) as f:
            while line := f.readline().strip():
                wire, value = line.split(": ")
                wires[wire] = int(value)
            while line := f.readline().strip():
                wire1, op, wire2, _, wire = line.split()
                gates[wire] = (wire1, op, wire2)
        return wires, gates
    
    def execute_gate(wire):
        wire1, op, wire2 = gates[wire]
        if not wire1 in wires:
            execute_gate(wire1)
        if not wire2 in wires:
            execute_gate(wire2)
        
        match op:
            case "AND":
                wires[wire] = wires[wire1] & wires[wire2]
            case "OR" :
                wires[wire] = wires[wire1] | wires[wire2]
            case "XOR":
                wires[wire] = wires[wire1] ^ wires[wire2]
    
    def execute_all():
        for i in range(0, WIRE_MAX + 1):
            wire = f"z{i:02}"
            execute_gate(wire)
    
    def compute_result():
        result = 0
        for i in range(WIRE_MAX, -1, -1):
            wire = f"z{i:02}"
            result <<= 1
            result |= wires[wire]
        return result
    
    wires, gates = read_input()
    execute_all()
    return compute_result()

if __name__ == "__main__":
    print(solution(INPUT_FILE))
