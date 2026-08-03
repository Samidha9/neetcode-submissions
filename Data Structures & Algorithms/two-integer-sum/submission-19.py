class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i, n in enumerate(nums):
            x = target - n
            if x in dict1:
                return [dict1[x] , i]
            else:
                dict1[n] = i