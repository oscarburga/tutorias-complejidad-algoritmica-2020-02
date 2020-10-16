H, W = map(int, input().split())

grid = [str() for j in range(H)]
for i in range(H):
	grid[i] = input()

dp = [[0 for x in range(W+1)] for y in range(H+1)]
dp[1][1] = 1
mod = (10**9) + 7

#dp[i][j]: Cantidad de caminos desde (1, 1) hasta (i, j)
for i in range(1, H+1):
	for j in range(1, W+1):
		dp[i][j] += dp[i-1][j] + dp[i][j-1]
		dp[i][j] *= grid[i-1][j-1] == '.'
		dp[i][j] %= mod

print(dp[H][W])
