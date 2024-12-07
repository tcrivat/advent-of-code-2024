INPUT_FILE = "input.txt"

def solution(filename):
    def solve(line):
        test_value, numbers = line.split(": ")
        test_value = int(test_value)
        numbers = list(map(int, numbers.split()))
        
        possible = {numbers[0]} # set
        for i in range(1, len(numbers)):
            possible = ({n + numbers[i] for n in possible} |
                        {n * numbers[i] for n in possible})
        
        return test_value if test_value in possible else 0
        
    with open(filename) as f:
        return sum(solve(line.strip()) for line in f)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
