class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = 0
        res = 0
        list1=[]
        for i, n in enumerate(nums):
            cursum = cursum + n
            if cursum >= n:
                list1.append(cursum)
            else:
                cursum = n
                list1.append(cursum)
        
        res=list1[0]
        for i in list1:
            if i >= res:
                res = i
        return res 