class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i,n in enumerate(nums):
            ans = target - n
            if ans in dict1:
                return [dict1[ans], i]
            else:
                dict1[n] = i