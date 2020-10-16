import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())

#n, m = [int(x) for x in input().split()]

res = [[-1 for x in range(m+1)] for y in range(n+1)]

def bt(i, j):
	if i == n and j == m: return 1
	if res[i][j] != -1: return res[i][j]
	ans = 0
	if i < n: ans += bt(i+1, j)
	if j < m: ans += bt(i, j+1)
	res[i][j] = ans
	return ans

print(bt(1, 1))
