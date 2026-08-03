class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_A = set(nums) 
        print(set_A)       
        if len(nums) > len(set_A):
            return True
        else:
            return False
        