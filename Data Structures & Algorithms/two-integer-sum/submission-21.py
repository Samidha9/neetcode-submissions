class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       dict1 = {}
       for i, val in enumerate(nums):
        x = target - val
        if x in dict1:
            return [dict1[x], i]
        else:
            dict1[val] = i