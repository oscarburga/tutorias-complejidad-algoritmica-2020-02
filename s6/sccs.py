import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
# vs[0]: grafo original
# vs[1]: grafo transpuesto
vs = [[[] for i in range(n)] for x in range(2)]
for i in range(m): # leer grafo
	x, y = map(int, input().split())
	x -= 1
	y -= 1
	vs[0][x].append(y)
	vs[1][y].append(x)


vis, topo = [False]*n, []
def dfs_topo(v):
	vis[v] = True
	for e in vs[0][v]:
		if not vis[e]:
			dfs_topo(e)
	topo.append(v)

for i in range(n):
	if not vis[i]:
		dfs_topo(i)
topo.reverse()

cnt, tag = 0, [-1] * n 
def dfs_scc(v):
	tag[v] = cnt
	for e in vs[1][v]: #grafo transpuesto!
		if tag[e] == -1:
			dfs_scc(e)
for v in topo:
	if tag[v] == -1:
		dfs_scc(v)
		cnt += 1

print(cnt)
for v in tag: print(v+1, end=' ')
print()

