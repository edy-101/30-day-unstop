from collections import deque


def user_logic(H, W, grid, queries):
    """
    Write your logic here.
    Parameters:
        H (int): Height of the grid
        W (int): Width of the grid
        grid (list of list of int): 2D list representing heights of cells in the grid
        queries (list of tuple): List of tuples representing each query (r, c, p)
    Returns:
        list of int: Computed result based on the problem statement
    """

    
    result = []
    
    for r, c, p in queries:
        r -= 1
        c -= 1
        
        if grid[r][c] >= p:
            result.append(0)
            continue
        
        visited = [[False] * W for _ in range(H)]
        q = deque()
        q.append((r, c))
        visited[r][c] = True
        count = 0
        
        while q:
            x, y = q.popleft()
            count += 1
            
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < H and 0 <= ny < W:
                    if not visited[nx][ny] and grid[nx][ny] < p:
                        visited[nx][ny] = True
                        q.append((nx, ny))
        
        result.append(count)
    
    return result





def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    index = 0
    
    H = int(data[index])
    index += 1
    W = int(data[index])
    index += 1
    Q = int(data[index])
    index += 1
    
    grid = []
    for i in range(H):
        row = list(map(int, data[index:index + W]))
        grid.append(row)
        index += W
    
    queries = []
    for i in range(Q):
        r = int(data[index])
        index += 1
        c = int(data[index])
        index += 1
        p = int(data[index])
        index += 1
        queries.append((r, c, p))
    
    # Call user logic function and get the output
    result = user_logic(H, W, grid, queries)
    
    # Print the output in the required format
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
