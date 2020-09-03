### Ver archivo LC-max-subarray.py para el link al problema

def merge(a, l, mid, r):
	cur = a[mid]
	maxl = cur
	for i in range(mid-1, l-1, -1):
		cur += a[i]
		maxl = max(maxl, cur)
	cur = a[mid+1]
	maxr = cur
	for i in range(mid+2, r+1):
		cur += a[i]
		maxr = max(maxr, cur)
	return maxl + maxr
	
def solve(a, l, r):
	if l == r:
		return a[l]
	mid = (l+r)//2
	left = solve(a, l, mid)
	right = solve(a, mid+1, r)
	combined = merge(a, l, mid, r)
	return max(left, right, combined)

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(solve(arr, 0, len(arr)-1))
arr = [-2,-1]
print(solve(arr, 0, len(arr)-1))
