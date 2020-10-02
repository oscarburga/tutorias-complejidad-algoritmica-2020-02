import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

from collections import deque

E = int(input())

vs = [[] for i in range(E)]

for i in range(E):
	line = list(input().split())
	for friend in line[1:]:
		vs[i].append(int(friend))

def solve():
	dis, cnt = [-1] * E, [0] * E
	source = int(input())
	if len(vs[source]) == 0:
		print(0)
		return
	dis[source] = 0
	q = deque([source])
	while len(q):
		v = q.popleft()
		cnt[dis[v]] += 1
		for e in vs[v]:
			if dis[e] == -1:
				dis[e] = dis[v] + 1
				q.append(e)
	mx, d = 0, -1
	for i in range(E):
		if cnt[i] > mx:
			mx = cnt[i]
			d = i
	print(mx, d)

T = int(input())
while T > 0:
	solve()
	T -= 1
