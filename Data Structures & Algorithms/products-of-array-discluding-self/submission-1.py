class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list1 = []
        prefix = 1
        for i in range(len(nums)):
            list1.append(prefix)
            prefix *= nums[i]

        suffix = 1
        x = len(list1)-1

        for i in range(len(nums)-1, -1, -1):
            list1[x] = list1[x] * suffix
            suffix *= nums[i]
            x -= 1
    
        
        return list1
        
