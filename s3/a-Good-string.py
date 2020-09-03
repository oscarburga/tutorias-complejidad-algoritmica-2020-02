'''
Link al problema: https://codeforces.com/contest/1385/problem/D
Resumen del problema:

Una cadena S[0..n] se define como C-good si se cumple al menos una de las siguientes condiciones:
	* La longitud de S es igual a 1, y su único caracter es la letra C
	* La longitud de S es mayor a 1, la primera mitad de S consiste únicamente de la letra
		C y la segunda mitad es una cadena (C+1)-good.
	* La longitud de S es mayor a 1, la segunda mitad de S consiste únicamente de la letra
		C y la primera mitad es una cadena (C+1)-good.

Se te pide determinar la mínima cantidad de letras que debes reemplazar para convertir a la cadena S
en una cadena a-good.

Para algunos ejemplos y el enunciadoo completo, ver el link del problema.
'''

infinity = 10**9

def inc_letter(x : str):
	return chr(ord(x) + 1)

def test_case():
	n = int(input())
	s = str(input())
	s = list(s)

	def solve(l : int = 0, r : int = n-1, f : str = 'a'):
		if ord(f) > ord('z'):
			return infinity
		if l == r:
			return int(s[l] != f)
		mid = (l+r)//2
		### Primera opción: volver la primera mitad toda igual a f, y la segunda mitad (f+1)-good
		costL = 0
		for x in s[l:mid+1]: costL += int(x != f)
		costL += solve(mid+1, r, inc_letter(f))
		### Segunda opción: segunda mitad igual a f, primera mitad (f+1)-good
		costR = 0
		for x in s[mid+1:r+1]: costR += int(x != f)
		costR += solve(l, mid, inc_letter(f))
		return min(costL, costR)
	
	print(solve())

test_cases = int(input())
while test_cases > 0:
	test_case()
	test_cases -= 1
