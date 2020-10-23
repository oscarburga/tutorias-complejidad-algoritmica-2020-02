#Minimizing Lateness
#Ojala consiga un link para la tutoria :(

n = int(input())
t, d = [0] * n, [0] * n

for i in range(n):
	t[i], d[i] = map(int, input().split())

p = [i for i in range(n)]

def keyf(x): return d[x]
p.sort(key=keyf)

ans = 0
curt = 0
for i in p:
	curt += t[i] 
	ans = max(ans, curt - d[i])
print(ans)
