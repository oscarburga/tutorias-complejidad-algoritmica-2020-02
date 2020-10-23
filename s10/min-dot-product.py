# https://vjudge.net/problem/CodeChef-BITMASK2

tc = int(input())
while tc > 0:
	n = int(input())
	a = [int(x) for x in input().split()]
	b = [int(x) for x in input().split()]
	a.sort()
	b.sort()
	b.reverse()
	ans = 0
	for i in range(n): ans += a[i] * b[i]
	print(ans)
	tc -= 1
