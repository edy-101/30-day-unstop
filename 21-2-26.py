def user_logic(n, tasks, W):
    if W > n:
        return -1

    left = max(tasks)
    right = sum(tasks)
    ans = right

    while left <= right:
        mid = (left + right) // 2
        workers = 1
        current = 0

        for t in tasks:
            if current + t > mid:
                workers += 1
                current = t
            else:
                current += t

        if workers <= W:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    tasks = list(map(int, data[1:n+1]))
    W = int(data[n+1])
    
    result = user_logic(n, tasks, W)
    print(result)

if __name__ == "__main__":
    main()
