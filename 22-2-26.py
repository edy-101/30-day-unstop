def maximum_weight_paths(n, edges, q, queries):
    edges.sort(key=lambda x: x[2])
    indexed_queries = sorted(enumerate(queries), key=lambda x: x[1])
    
    parent = list(range(n + 1))
    size = [1] * (n + 1)
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return 0
        if size[rx] < size[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        paths = size[rx] * size[ry]
        size[rx] += size[ry]
        return paths
    
    res = [0] * q
    total = 0
    i = 0
    
    for idx, val in indexed_queries:
        while i < len(edges) and edges[i][2] <= val:
            u, v, _ = edges[i]
            total += union(u, v)
            i += 1
        res[idx] = total
    
    return res



def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    index = 0
    n = int(data[index])
    index += 1
    edges = []
    for _ in range(n - 1):
        u = int(data[index])
        v = int(data[index + 1])
        w = int(data[index + 2])
        edges.append((u, v, w))
        index += 3
    q = int(data[index])
    index += 1
    queries = []
    for _ in range(q):
        queries.append(int(data[index]))
        index += 1
    result = maximum_weight_paths(n, edges, q, queries)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
