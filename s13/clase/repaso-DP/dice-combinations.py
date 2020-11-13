import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

# Contar la cantidad de formas de sumar N utilizando
# numeros del 1 al 6

# Si te piden modulo 10^9 + 7 significa
# que debes hacer todos tus calculos modulo 10^9 + 7 (menos division)
mod = (10**9) + 7
def add(x, y): return (x+y) % mod;
def sub(x, y): return (((x-y)%mod)+mod) % mod
def mul(x, y): return (x*y) % mod;

'''
dp[i]: cantidad de formas de sumar i
dp[0]: 1
en cada "turno" nuestro dado puede dar 1 de 6 resultados:
1, 2, 3, 4, 5, 6

saco 1: dp[x] = dp[x-1]
saco 2: dp[x] = dp[x-2]
saco 3: dp[x] = dp[x-3]
...

simplemente, dp[x] es la suma de dp[x-6], dp[x-5] ... dp[x-1]
'''
n = int(input())
dp = [0] * (n+1)
dp[0] = 1

for i in range(1, n+1):
	#tengo que sumar dp[i-6], dp[i-5]... dp[i-1]
	for j in range(1, 7):
		if i - j >= 0:
			dp[i] = add(dp[i], dp[i-j])

print(dp[n])
