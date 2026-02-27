def user_logic(n, maxBooks, k, books):
    INF = 10**18
    states = {(0, 0, 0): 0}
    for a in books:
        nexts = {}
        for (d, cnt, m), cost in states.items():
            if d < k:
                key = (d + 1, cnt, m)
                prev = nexts.get(key)
                if prev is None or cost < prev:
                    nexts[key] = cost
            if cnt + 1 < maxBooks:
                nm = a if cnt == 0 else (m if m >= a else a)
                key = (d, cnt + 1, nm)
                prev = nexts.get(key)
                if prev is None or cost < prev:
                    nexts[key] = cost
            else:
                nm = a if cnt == 0 else (m if m >= a else a)
                key = (d, 0, 0)
                val = cost + nm
                prev = nexts.get(key)
                if prev is None or val < prev:
                    nexts[key] = val
            if cnt > 0:
                closecost = cost + m
                if d < k:
                    key = (d + 1, 0, 0)
                    prev = nexts.get(key)
                    if prev is None or closecost < prev:
                        nexts[key] = closecost
                if maxBooks > 1:
                    key = (d, 1, a)
                    prev = nexts.get(key)
                    if prev is None or closecost < prev:
                        nexts[key] = closecost
                else:
                    key = (d, 0, 0)
                    val = closecost + a
                    prev = nexts.get(key)
                    if prev is None or val < prev:
                        nexts[key] = val
        states = nexts
    ans = INF
    for (d, cnt, m), cost in states.items():
        if d <= k:
            total = cost + (m if cnt > 0 else 0)
            if total < ans:
                ans = total
    return ans

def main():
    import sys
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    maxBooks = int(data[1])
    k = int(data[2])
    books = list(map(int, data[3:]))
    result = user_logic(n, maxBooks, k, books)
    print(result)

if __name__ == "__main__":
    main()
