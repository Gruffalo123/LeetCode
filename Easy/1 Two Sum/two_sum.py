class Solution:
    def twoSum(self, nums, target):
        for i, n in enumerate(nums):
            if target - n in nums and nums.index(target - n) != i:
                return sorted([i, nums.index(target - n)])

nums=[2,7,11,15]
target = 9
s = Solution()
a = s.twoSum(nums,target)
print(a)

nums1=[3,2,4]
target1 = 6
s1 = Solution()
a1 = s.twoSum(nums1,target1)
print(a1)

nums2=[3,3]
target2 = 6
s2 = Solution()
a2 = s.twoSum(nums2,target2)
print(a2)