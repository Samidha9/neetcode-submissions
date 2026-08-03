class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''lp = 0
        rp = 1
        cursum = 0
        for i in range(len(nums)):
            runsum = nums[i]
            cursum = cursum + runsum
            print(cursum)
            if cursum >= nums[rp]:
                rp += 1
            else:

                lp += 1'''
        
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
        print(list1)
        res=list1[0]
        print(res)
        for i in list1:
            if i >= res:
                res = i
        return res 