n, W = map(int, input().split())
w, v = [0] * n, [0] * n

maxval = 0
for i in range(n):
	w[i], v[i] = map(int, input().split())
	maxval += v[i]

inf = 10**18
dp = [inf for x in range(maxval+1)]
dp[0] = 0;

#Recurrencia distinta: dp[j]: minimo peso para obtener el valor j
for i in range(n):
	for j in reversed(range(v[i], maxval+1)):
		dp[j] = min(dp[j], dp[j-v[i]] + w[i])

for j in reversed(range(maxval+1)):
	if dp[j] <= W:
		print(j)
		break
