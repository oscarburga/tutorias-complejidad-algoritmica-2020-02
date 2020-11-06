import heapq as hp
n, m = map(int, input().split())

vs = [[] for i in range(n)]
for i in range(m):
	x, y, w = map(int, input().split())
	vs[x-1].append((w, y-1))


def dijkstra(src = 0):
	inf = 10**18
	d = [inf] * n
	d[src] = 0
	q = [(0, src)]
	vis = [False] * n
	while len(q):
		_, v = hp.heappop(q)
		if vis[v]: continue
		vis[v] = True
		for w, e in vs[v]:
			if d[v] + w < d[e]:
				d[e] = d[v] + w
				hp.heappush(q, (d[e], e))
	return d

dis = dijkstra(0)
for i in range(n): print(dis[i], sep='', end=' \n'[i+1==n])
