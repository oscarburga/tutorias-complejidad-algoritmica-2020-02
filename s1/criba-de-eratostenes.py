### https://nbviewer.jupyter.org/github/racsosabe/Miscelanea/blob/master/UPC/Clase%2008%20-%20Teor%C3%ADa%20de%20N%C3%BAmeros%20I.ipynb?fbclid=IwAR043EmUu_SSOm9ulgfgBKjkpDZX1MRMXhNgYaGap730RFTE6KWiiPESjOo
### https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html

n = int(input())

def criba_clasica(n):
	prime = [True] * (n+1) ### Asumo que todos son primos al inicio
	primes = []  ### Lista donde agrego los numeros primos encontrados
	prime[0] = prime[1] = False
	for i in range(2, n+1):
		if prime[i]:
			primes.append(i)
			for j in range(i+i, n+1, i):
				prime[j] = False
	return prime, primes

def criba_optimizada(n):
	prime = [True] * (n+1) 
	primes = []  
	prime[0] = prime[1] = False
	i = 2
	while i*i <= n:  ### Solo es necesario recorrer hasta la raiz de N
		if prime[i]:
			primes.append(i)
			for j in range(i*i, n+1, i): ### Solo es necesario recorrer desde el cuadrado de i
				prime[j] = False
		i += 1
	### La complejidad de esta optimización es O(n*log(log(raiz(n)))), que es equivalente a O(nloglogn)
	### Sin embargo, si reduce el factor constante considerablemente.
	return prime, primes

### Optimización adicional (ejercicio): 
### Como todos los numeros primos son impares (a excepción del 2), modifique la criba para que 
### el loop principal solo recorra los números impares. ¿Esta optimización modifica la complejidad?

is_prime, primes = criba_clasica(n)
print(primes)
