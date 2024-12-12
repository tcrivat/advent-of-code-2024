INPUT_FILE = "input.txt"

def convert(disk_map):
    """Convert to a new list with [id, size] elements."""
    new_disk_map = []
    for i in range(len(disk_map)):
        if i % 2: # free space
            new_disk_map.append([-1, disk_map[i]])
        else: # file
            new_disk_map.append([i // 2, disk_map[i]])
    return new_disk_map

def rearrange(disk_map):
    """Rearrange the files accordig to the rules."""
    min_left = [0] * 10
    right = len(disk_map) - 1
    while True:
        while right >= 0 and disk_map[right][0] == -1:
            right -= 1
        if right < 0:
            break
        size = disk_map[right][1]
        left = min_left[size]
        while True:
            while left <= right and disk_map[left][0] != -1:
                left += 1
            if left >= right:
                break
            if disk_map[left][1] >= size:
                disk_map[left][1] -= size
                file = disk_map[right]
                disk_map[right] = [-1, size]
                disk_map.insert(left, file)
                left += 1
                break
            left += 1
        while size < 10 and left > min_left[size]:
            min_left[size] = left
            size += 1
        right -= 1
    return disk_map

def checksum(disk_map):
    """Compute the checksum."""
    sum = 0
    poz = 0
    for file in disk_map:
        if file[0] != -1:
            sum += file[0] * file[1] * (2 * poz + file[1] - 1) // 2
        poz += file[1]
    return sum

def solution(filename):
    with open(filename) as f:
        disk_map = list(map(int, f.readline().strip()))
    return checksum(rearrange(convert(disk_map)))

if __name__ == "__main__":
    print(solution(INPUT_FILE))
