tc = int(input())

while tc > 0:
	n = int(input())
	A = [int(x) for x in input().split()]
	B = [int(x) for x in input().split()]
	A.sort()
	B.sort(reverse=True)
	ans = 0
	for i in range(n): ans += A[i] * B[i]
	print(ans)
	tc -= 1

