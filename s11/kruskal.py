import heapq as hp

inf = 10**9

n, m = map(int, input().split())
edges = [(0, 0, 0) for x in range(m)]

p, sz= [-1] * n, [1] * n
def find(x): #Compresión de caminos
	if p[x] == -1: return x
	p[x] = find(p[x])
	return p[x]

def join(ed): #Optimización de union por tamaños
	x, y = find(ed[1]), find(ed[2])
	if x == y: return 0
	if sz[x] < sz[y]: 
		sz[y] += sz[x]
		p[x] = y
	else:
		sz[x] += sz[y]
		p[y] = x
	return ed[0]

for i in range(m):
	x, y, w = map(int, input().split())
	edges[i] = (w, x, y)

edges.sort()
ans = 0
for e in edges: ans += join(e)
print(ans)		
