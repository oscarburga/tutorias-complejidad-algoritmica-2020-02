### https://leetcode.com/problems/maximum-subarray/

class Solution:
    def merge(self, a, l, mid, r) -> int:
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
    
    def solve(self, a, l, r) -> int:
        if l == r:
            return a[l]
        mid = (l+r)//2
        left = self.solve(a, l, mid)
        right = self.solve(a, mid+1, r)
        combined = self.merge(a, l, mid, r)
        return max(left, right, combined)
    
    def maxSubArray(self, nums: List[int]) -> int:
        return self.solve(nums, 0, len(nums)-1)
        
