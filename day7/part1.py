import operator

INPUT_FILE = "input.txt"

def solution(filename):
    def solve(line):
        test_value, numbers = line.split(": ")
        test_value = int(test_value)
        numbers = list(map(int, numbers.split()))
        operators = [operator.add,
                     operator.mul]
        
        possible = {numbers[0]} # set
        for i in range(1, len(numbers)):
            possible = {r for n in possible
                          for op in operators
                          if (r := op(n, numbers[i])) <= test_value}
        
        return test_value if test_value in possible else 0
        
    with open(filename) as f:
        return sum(solve(line.strip()) for line in f)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
