#3 lineas para alzar el limite de la recursion
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())

vs = [[] for i in range(n)]
for i in range(m):
	x, y = map(int, input().split())
	vs[x-1].append(y-1)

#como hallar un ordenamiento topologico:
#empezamos asumiendo que nuestro grafo dirigido no tiene ciclos

# 0: no lo he visitado para nada
# 1: actualmente lo estoy procesando
# 2: ya lo procesé antes
vis = [False] * n

topo = []
def dfs(v):
	vis[v] = True
	for e in vs[v]:
		if not vis[e]:
			dfs(e)
	topo.append(v)

dfs(0)
if not vis[n-1]:
	print("IMPOSSIBLE")
	exit()

topo.reverse()
lp = [1] * n #longest path
p = [-1] * n #padre
for v in topo: 
	for e in vs[v]:
		if lp[v] + 1 > lp[e]:
			lp[e] = lp[v] + 1
			p[e] = v

path = []
v = n-1
while v != -1:
	path.append(v)
	v = p[v]

path.reverse()
print(lp[n-1])
for x in path: print(x+1, end=' \n'[x==path[-1]])
