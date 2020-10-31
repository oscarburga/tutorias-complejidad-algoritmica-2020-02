# Aplicacion interesante de DSU
# No hubo tiempo para verlo en clase, ojala lo podamos ver más adelante
# https://csacademy.com/ieeextreme-practice/task/rescue-mission/
n = int(input())
s = [int(x) for x in input().split()]

### DSU
p = [-1] * n
llink = [i for i in range(n)]
rlink = llink.copy()
## No usamos arreglo para la cantidad de soldados
## Para ello reciclaremos el arreglo 's'

def find(x): # El find igual que siempre, con compresión de caminos
	if p[x] == -1: return x
	p[x] = find(p[x])
	return p[x]

def join(l, r): 
	i = rlink[l] + 1
	u = find(l)
	while i <= r:
		v = find(i)
		if u != v: # No usamos heurística de tamaño/rango
			s[u] += s[v]
			rlink[u] = max(rlink[u], rlink[v])
			llink[u] = min(llink[u], llink[v])
			p[v] = u
		i = rlink[u] + 1 #Siempre saltamos al inicio del sgte intervalo

d = int(input())

ans = 0
while d > 0:
	d -= 1
	l, r, v = map(int, input().split())
	l -= 1
	r -= 1
	join(l, r)
	u = find(l)
	ans += min(v, s[u])
	s[u] -= min(v, s[u])
print(ans)
