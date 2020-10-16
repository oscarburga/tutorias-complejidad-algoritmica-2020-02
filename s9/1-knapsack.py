n, W = map(int, input().split())
w, v = [0] * n, [0] * n

for i in range(n):
	w[i], v[i] = map(int, input().split())

inf = 10**18
dp = [-inf for x in range(W+1)]
dp[0] = 0;

#dp[j]: minimo costo para obtener el peso 'j'
for i in range(n):
	for j in reversed(range(w[i], W+1)):
		dp[j] = max(dp[j], dp[j-w[i]] + v[i])

print(max(dp))
