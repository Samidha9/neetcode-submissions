class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list1 = []
        prefix = 1
        for i in range(len(nums)):
            list1.append(prefix)
            prefix *= nums[i]

        list2 = []
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            list2.append(suffix)
            suffix *= nums[i]
        x = 0
        for i in range(len(list2) -1 , -1, -1):
            list1[x] = list1[x] * list2[i]
            x += 1
        
        return list1
        
