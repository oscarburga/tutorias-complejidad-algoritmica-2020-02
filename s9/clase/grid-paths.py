n = int(input())
grilla = [str() for x in range(n)]

for i in range(n):
	grilla[i] = input()
	
dp = [[0 for x in range(n+1)] for j in range(n+1)]

mod = (10**9) + 7
dp[1][1] = int(grilla[0][0] == '.')
for i in range(1, n+1):
	for j in range(1, n+1):
		if grilla[i-1][j-1] == '.':
			dp[i][j] += dp[i-1][j] + dp[i][j-1]
			dp[i][j] %= mod
print(dp[n][n])
