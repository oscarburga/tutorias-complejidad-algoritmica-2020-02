import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
vs = [[[] for x in range(n)] for j in range(2)]
vis = [False] * n

# vs[0] es el grafo original
# vs[1] es el transpuesto
for i in range(m):
	x, y = map(int, input().split())
	x-=1
	y-=1
	vs[0][x].append(y)
	vs[1][y].append(x)

topo = []
def dfs1(v):
	vis[v] = True
	for e in vs[0][v]: #grafo original
		if not vis[e]:
			dfs1(e)
	topo.append(v)

cnt = 0
tag = [-1] * n
def dfs2(v):
	vis[v] = True
	tag[v] = cnt
	for e in vs[1][v]: #grafo transpuesto
		if not vis[e]:
			dfs2(e)

for i in range(n):
	if not vis[i]:
		dfs1(i)

topo.reverse()
vis = [False] * n
for v in topo:
	if not vis[v]:
		dfs2(v)
		cnt += 1

for i in range(n):
	print(i+1, ": ", tag[i])


