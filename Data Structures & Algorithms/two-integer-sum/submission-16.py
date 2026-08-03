class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for index, value in enumerate(nums):
            temp=target-value
            if temp in dict1:
                return [dict1[temp], index]
            else:
                dict1[value]=index