INPUT_FILE = "input.txt"

def solution(filename):
    with open(filename) as f:
        disk_map = list(map(int, f.readline().strip()))
    checksum = 0
    left = 0
    right = len(disk_map) - 1
    if right % 2: # ignore free space at the end
        right -= 1
    poz = 0
    while left <= right:
        if left % 2: # free space
            while disk_map[left]:
                while not disk_map[right]:
                    right -= 2
                id = right // 2
                size = min(disk_map[left], disk_map[right])
                checksum += id * size * (2 * poz + size - 1) // 2
                poz += size
                disk_map[left] -= size
                disk_map[right] -= size
        else: # file
            id = left // 2
            size = disk_map[left]
            checksum += id * size * (2 * poz + size - 1) // 2
            poz += size
        left += 1
    return checksum

if __name__ == "__main__":
    print(solution(INPUT_FILE))
