import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
vs = [[] for i in range(n)]
for i in range(m):
	x, y = map(int, input().split())
	vs[x-1].append(y-1)

vis = [int(0)] * n
topo = []
def dfs(v):
	vis[v] = 1
	for e in vs[v]:
		if vis[e] == 0:
			dfs(e)
		elif vis[e] == 1:
			print("IMPOSSIBLE")
			exit()
	vis[v] = 2
	topo.append(v)
	
for i in range(n):
	if vis[i] == 0:
		dfs(i)

topo.reverse()
for v in topo: print(v+1, end=' \n'[v==topo[-1]])
