import sys

def maximizeTasks(energy, power):
    energy.sort()
    power.sort()
    i = 0
    j = 0
    count = 0
    while i < len(energy) and j < len(power):
        if energy[i] <= power[j]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1
    return count

if __name__ == '__main__':
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    energy = list(map(int, data[2:n+2]))
    power = list(map(int, data[n+2:n+2+m]))
    maxTasks = maximizeTasks(energy, power)
    print(maxTasks)
