class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        if not nums:
            return 0
        list1 = []
        for i in nums:
            if i - 1 not in nums:
                count = 1
                x = i+1
                while x in nums:
                    count += 1
                    x += 1
                list1.append(count)
        return max(list1)         