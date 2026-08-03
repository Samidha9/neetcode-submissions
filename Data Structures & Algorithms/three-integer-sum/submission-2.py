class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''nums.sort()
        print(nums)
        list1=[]
        for i in range(len(nums) - 2):
            lp = i+1
            rp = len(nums) - 1
            while lp < rp:
                add = nums[lp] + nums[rp]
                if add + i == 0:
                    list1.append([nums[i], nums[lp], nums[rp])
                elif add + nums[i] > 0:
                    rp -= 1
                else:
                    lp += 1
        
        list2=[]
        for i in list1:
            if i not in list2:
                list2.append(i)
        return list2'''

        list1 = []
        list2 = []
        list3 = []
        for i in nums:
            if i < 0:
                list1.append(i)
            if i > 0:
                list2.append(i)
            if i == 0:
                list3.append(i)
        if not list1 and len(list3) < 3 or not list2 and len(list3) < 3:
            return []
        nums.sort()
        list4 =[]
        for i in range(len(nums) - 2):
            lp = i+1
            rp = len(nums) - 1
            while lp < rp:
                add = nums[lp] + nums[rp]
                if add + nums[i] == 0:
                    list4.append([nums[i], nums[lp], nums[rp]])
                    lp += 1
                elif add + nums[i] > 0:
                    rp -= 1
                else:
                    lp += 1

        list5 = []
        for i in list4:
            if i not in list5:
                list5.append(i)
        return list5





















        '''res = []
        nums.sort()
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1              
        return res'''