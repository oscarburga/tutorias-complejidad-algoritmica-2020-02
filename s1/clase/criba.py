n = int(input())

primo = [True] * (n+1)
for i in range(2, n+1):
	if primo[i]:
		for j in range(i+i, n+1, i):
			primo[j] = False
		
## O(N^2) ???? -> NOP

for i in range(2, n+1):
	### Este segundo for hace n/i operaciones
	for j in range(i+i, n+1, i): ## empiezo en 2*i -> 3*i -> 4*i...
		primo[j] = False

## Sin el if, es O(NlogN)
## Con el if, la complejidad baja a O(N*log(log(N)))
