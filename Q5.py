import sys

def min_cost_path():
    R = int(input())
    C = int(input())
    M = int(input())

    grid = []
    for i in range(R):
        row = []
        for j in range(C):
            row.append((i * C + j) % M + 1)
        grid.append(row)    
    dp = []
    for _ in range(R):
        row = [float("inf")] * C
        dp.append(row)
    for c in range(C):
        dp[0][c] = grid[0][c]
    for r in range(1, R):
        for c in range(C):
            dp[r][c] = grid[r][c] + min(
                dp[r - 1][c - 1] if c > 0 else float("inf"),
                dp[r - 1][c],
                dp[r - 1][c + 1] if c < C - 1 else float("inf")
            )

    print(min(dp[R - 1]))
if __name__ == "__main__":
    min_cost_path()
