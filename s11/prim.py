import heapq as hp

inf = 10**9

n, m = map(int, input().split())
c = [inf] * n
vis = [False] * n
vs = [[] for x in range(n)]

for i in range(m):
	x, y, w = [int(x) for x in input().split()]
	vs[x].append((y, w))
	vs[y].append((x, w))

q = [(0, 0)]
c[0] = 0
ans = 0
while len(q):
	_, v = hp.heappop(q)
	if vis[v]: continue
	vis[v] = True
	ans += c[v]
	for e, w in vs[v]: 
		if w < c[e] and (not vis[e]):
			c[e] = w
			hp.heappush(q, (w, e))
print(ans)		
