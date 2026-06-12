class Solution:
    def bubble_sort(self, arr:List[int]) -> List[List[int]]:
        n = len(arr)
        for i in range(n):
            swapped = False

            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped =True

            if not swapped:
                break
        return arr
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = self.bubble_sort(nums)
        res = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j=i+1
            k=n-1
            target = -nums[i]
        
            while j < k:
                total = nums[j] + nums[k]
                if total < target:
                    j = j + 1
                elif total > target:
                    k = k - 1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j]==nums[j-1]:
                        j+=1
        return res
            