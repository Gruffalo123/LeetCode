class Solution:
    def twoSum(self, nums, target):
        for i in nums:
            for j in nums:
                if int(i) + int(j) == target and int(i) != int(j):
                    return [nums.index(int(i)), nums.index(int(j))]


nums=[2,7,11,15]
target = 9
s = Solution()
a = s.twoSum(nums,target)
print(a)